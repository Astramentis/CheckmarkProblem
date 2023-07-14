from tools import Timer
import sqlite3
import openai
import key
import string
openai.api_key = key.AIkey

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

#sentiment = sentiment_analysis("TESTING TESTING 123")
#print(sentiment)
#print("finished")


#dataset credits: https://www.kaggle.com/datasets/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows?select=0825_UkraineCombinedTweetsDeduped.csv.gzip

