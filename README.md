# 🔌 Twitter Sentiment Analysis API (Flask + MongoDB + ML)

## 📖 Sobre o Projeto

Esta é a camada de produção do projeto. Ela consiste em uma **API RESTful** que automatiza o ciclo completo de vida do dado: extração em tempo real do Twitter, pré-processamento, classificação via Machine Learning e persistência em um banco de dados NoSQL.

## 🛠️ Arquitetura e Estrutura de Arquivos

A aplicação foi desenvolvida de forma modular para facilitar a manutenção e escalabilidade:

 - `app.py`: O coração da aplicação. Gerencia as rotas Flask e orquestra a chamada de todos os outros módulos.

- `extrai_tweets.py`: Módulo responsável pela integração com a API do Twitter via Tweepy.

- `limpa_texto.py`: Script de NLP para limpeza e normalização dos dados brutos (Regex, remoção de caracteres especiais).

- `classifica_sentimento.py`: Carrega o modelo de Machine Learning e o vetorizador para realizar a inferência (predição) nos novos tweets.

- Modelos e Pesos:

  - `classification.model`: O modelo de ML treinado e serializado.

  - `vectorizer.pickle`: O transformador TF-IDF utilizado para processar os textos antes da predição.

- Segurança:

  - `twitterpass.py / mongopass.py`: Scripts dedicados para gestão segura de credenciais (Configurados para evitar exposição de chaves).

- Testes:

  - `curl_command.txt`: Exemplos de comandos cURL para validar os endpoints da API.

## 🚀 Fluxo da API

1. A API recebe uma requisição (ex: uma palavra-chave para busca).

2. O `extrai_tweets.py` busca os dados no Twitter.

3. O `limpa_texto.py` sanitiza as mensagens.

4. O `classifica_sentimento.py` usa o .model e .pickle para prever a polaridade (Positivo/Negativo).

5. O `resultado é enviado` para o **MongoDB** e retornado em formato **JSON** para o usuário.

## 🔧 Instalação e Uso

1. Clone o repositório:

```
git clone https://github.com/alan-vieira/api_analise_de_sentimento_twitter.git
```

2. Instale as dependências listadas no `requirements.txt`:

```
pip install -r requirements.txt
```

3. Configure suas chaves de API nos arquivos `twitterpass.py` e `mongopass.py`.

4. Execute o servidor:

```
python app.py
```

## 🧪 Exemplo de Requisição

Você pode testar a API utilizando o comando disponível no arquivo `curl_command.txt`. A resposta será um JSON contendo o texto original e o sentimento atribuído pelo modelo.

📺 Demonstração
Assista ao funcionamento da API e a integração com o banco de dados:

🔗 [Vídeo: Arquitetura da API e Deploy](https://www.youtube.com/watch?v=9D7xsx-Z_GU)

## 👤 Autor

**Alan Vieira** - *Engenheiro de Telecomunicações & Especialista em Dados*

- [LinkedIn](https://www.linkedin.com/in/alansilvavieira)

- [GitHub Portfólio](https://github.com/alan-vieira)
