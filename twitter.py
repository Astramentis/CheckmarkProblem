#pip install tweepy
#pip install OpenAI
from tools import Timer
import sqlite3
import openai
import key
import string
import tweepy
import ssl
import csv
openai.api_key = key.AIkey
auth = tweepy.OAuthHandler(key.twe_key , key.twe_key_secret)
auth.set_access_token(key.twe_token , key.twe_token_secret)
api = tweepy.API(auth)

def sentiment_analysis(text):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages=[
        {"role": "system", "content": "You are performing text analysis."},
        {"role": "user", "content": "Yes or no only, is the following comment toxic: " + text},
        ],
        temperature = 0,    
        max_tokens = 250,
    )
    message = response["choices"][0]["message"]["content"].strip().lower().translate(str.maketrans('', '', string.punctuation))
    sentiment = None
    if "yes" in message:
        sentiment = "1"
    elif "no" in message:
        sentiment = "2"
    else:
        sentiment = "0"
    #ratelimit here
    return sentiment  

def tweet_pull(name,tweet_id):
    auth = tweepy.OAuthHandler(key.twe_key , key.twe_key_secret)
    auth.set_access_token(key.twe_token , key.twe_token_secret)
    api = tweepy.API(auth)
    ssl._create_default_https_context = ssl._create_unverified_context
    replies = []
    for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name,result_type='recent',timeout=999999).items(1000):
        print('here')
        if hasattr(tweet, 'in_reply_to_tweet_id'):
            if (tweet.in_reply_to_tweet_id==tweet_id):
                print(tweet)
                replies.append(tweet)


    with open('replies_clean.csv', 'wb') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
        csv_writer.writeheader()
        for tweet in replies:
            row = {'user': tweet.user.screen_name, 'text': tweet.text.encode('ascii', 'ignore').replace('\n', ' ')}
            csv_writer.writerow(row)            

tweet_pull('NateSilver538','1676980499410202624')


#sentiment = sentiment_analysis("TESTING TESTING 123")
#print(sentiment)
#print("finished")

