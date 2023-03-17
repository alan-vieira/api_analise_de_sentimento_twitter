import pickle

# Carrega do modelo classificador
def classifica_texto(texto):
    # carrega o vetorizador
    carrega_vetorizador = pickle.load(open('vectorizer.pickle', 'rb'))

    # carrega o modelo
    carrega_modelo = pickle.load(open('classification.model', 'rb'))

    # realiza a predição
    return carrega_modelo.predict(carrega_vetorizador.transform([texto]))
