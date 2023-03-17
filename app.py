import json
from bson.json_util import ObjectId

from flask import Flask, request, jsonify

from pymongo import MongoClient
from mongopass import mongopass

from extrai_tweets import pega_tweets
from limpa_texto import limpa_texto
from classifica_sentimento import classifica_texto


# JSON encoder customizado para converter ObjectIds em strings
class MeuEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MeuEncoder, self).default(obj)


# instanciando o flask
app = Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = MeuEncoder


# conexão com o banco de dados
client = MongoClient(mongopass)
db = client.senttwitter  # nome do banco
minhacolecao = db.tweets  # nome da coleção


# Enviar lista de trends, extrair tweets e classificar sentimento
@app.route('/tweets', methods=['POST'])
def processa_tweets():
    # envio da lista de trends
    lista = request.get_json().get('lista')

    # extração dos tweets baseados na lista
    tweet_df = pega_tweets(lista)

    # execução da etapa de pré-processamento
    tweet_df = limpa_texto(tweet_df)

    # execução da predição do sentimento
    tweet_df['sentiment'] = tweet_df['text_lemma'].apply(classifica_texto)

    # removendo os colchetes dos valores das células
    tweet_df['sentiment'] = tweet_df['sentiment'].apply(lambda x: (x[0]))

    # convertendo o dataframe em dicionário
    tweet_df.reset_index(inplace=True)
    tweet_dict = tweet_df.to_dict("records")

    # enviando a coleção de dados para o banco
    minhacolecao.insert_many(tweet_dict)

    return jsonify(message="Trabalho processado com sucesso")


# Consultar os tweets com o sentimento classificado
@app.route('/tweets', methods=['GET'])
def ver_tweets():
    tweets = minhacolecao.find()

    return jsonify(list(tweets))


# Limpar o banco de dados
@app.route('/tweets', methods=['DELETE'])
def limpa_banco():
    minhacolecao.drop()

    return jsonify(message="Banco limpo com sucesso")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
