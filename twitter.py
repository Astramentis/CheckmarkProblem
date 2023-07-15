from tools import Timer
import sqlite3
import openai
import key
import string
openai.api_key = key.AIkey
conn = sqlite3.connect('CheckMark.db')
cursor = conn.cursor()
t = Timer()

def text_analysis(text):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages=[
        {"role": "system", "content": "You are performing Flesch Kincaid grade level text analysis."},
        {"role": "user", "content": "Grade level reply only, what is the Flesch Kincaid grade level of the following passage: " + text},
        ],
        temperature = 0,    
        max_tokens = 350,
    )
    message = response["choices"][0]["message"]["content"].strip().lower().translate(str.maketrans('', '', string.punctuation))
    numeric = ''.join(filter(str.isdigit, message))
    #ratelimit here
    return message, numeric


analysis, numeric = text_analysis("The floor was covered with snow-white canvas, not laid on smoothly, but rumpled over bumps and hillocks, like a real snow field. The numerous palms and evergreens that had decorated the room, were powdered with flour and strewn with tufts of cotton, like snow. Also diamond dust had been lightly sprinkled on them, and glittering crystal icicles hung from the branches.")
print(analysis)
print(numeric)
print("finished")


#dataset credits: https://www.kaggle.com/datasets/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows?select=0825_UkraineCombinedTweetsDeduped.csv.gzip

