import time
import pandas as pd
import tweepy as tw
from tqdm import tqdm
from twitterpass import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

# autenticação da api do twitter
auth = tw.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)


def pega_tweets(trends):
    # teste de extração
    query_search = trends[0] + ' -filter:retweets'
    cursor_tweets = tw.Cursor(api.search_tweets,
                                        q=query_search,
                                        lang="pt").items(1)

    for tweet in cursor_tweets:
        tweet._json 


    tweet_keys = tweet._json.keys()
    tweet_dict = {}
    tweet_dict = tweet_dict.fromkeys(tweet_keys)
    tendencia = []

    # extração dos tweets
    for trend in trends:
        query_search = trend + ' -filter:retweets'
        cursor_tweets = tw.Cursor(api.search_tweets,
                                            q=query_search,
                                            lang="pt").items(200)


        for i, tweet in zip(tqdm(range(0,200), ncols = 100, desc = trend), cursor_tweets):
            time.sleep(.1)

            tendencia.append(trend)

            for key in tweet_dict.keys():
                try:
                    tweet_keys = tweet._json[key]
                    tweet_dict[key].append(tweet_keys)

                except KeyError:
                    tweet_keys = ""
                    tweet_dict[key].append("")
                except:
                    tweet_dict[key] = [tweet_keys]

    # transformando do dicionário em dataframe
    tweet_df = pd.DataFrame.from_dict(tweet_dict)
    tweet_df['trend_t'] = tendencia

    return tweet_df
