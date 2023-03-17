import nltk
import re

import spacy

from extrai_tweets import *


def remove_caracteres(instancia):
    ''' 
    Função de remoção de caracteres:
    'http\S+' - remove url 
    lower() - tranforma o texto em minúsculo
    '[0-9]+' - remove números
    '[^\w\s]' -  remove pontuação
    '[!#$%^&*()]' - remove caractéres espaciais
    '''
    instancia = re.sub(r'http\S+', '', instancia).lower()
    instancia = re.sub(r'[0-9]+', '', instancia)
    instancia = re.sub(r'[^\w\s]', '', instancia)
    instancia = re.sub('[!#$%^&*()]', '', instancia)
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (' '.join(palavras))

def remove_emojis(string):
    '''Função que remove emojis'''
    emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def limpa_texto(tweet_df):
    # separando apenas as variáveis que quero visualizar
    tweet_df = tweet_df[['text','trend_t']]

    # aplicando a limpeza dos dados
    tweet_df['text_clean'] = tweet_df['text'].apply(remove_caracteres).apply(remove_emojis)

    # lematização com spacy
    nlp = spacy.load('pt_core_news_sm')

    tweet_df['text_lemma'] = tweet_df['text_clean'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))
    tweet_df['text_lemma'] = tweet_df['text_lemma'].apply(str.lower)
    
    return tweet_df
