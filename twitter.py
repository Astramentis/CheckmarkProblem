import sqlite3
import openai
import key
import string
import traceback
import time
openai.api_key = key.AIkey
conn = sqlite3.connect('CheckMark.db')
cursor = conn.cursor()

def text_analysis(text):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages=[
        {"role": "system", "content": "You are performing Flesch Kincaid grade level text analysis."},
        {"role": "user", "content": "Grade level reply only, what is the Flesch Kincaid grade level of the following passage, ignoring symbols not relevant to the test: " + text},
        ],
        temperature = 0,    
        max_tokens = 350,
    )
    message = response["choices"][0]["message"]["content"].strip().lower().translate(str.maketrans('', '', string.punctuation))
    numeric = ''.join(filter(str.isdigit, message))
    #ratelimit here
    time.sleep(3)
    return message, numeric

cursor.execute("SELECT rowid, text FROM BitcoinFiltered WHERE GPT_Score IS NULL AND user_verified = 'True' ORDER BY RANDOM() LIMIT 500")
rows = cursor.fetchall()

# Perform text analysis on each excerpt and update table 
for row in rows:
    try:
        id  = row[0]
        text  = row[1]
        assessment,score = text_analysis(text)
        print(assessment)
        print(score)
        #remember change table! ↓ ↓ ↓ ↓ 
        cursor.execute("UPDATE BitcoinFiltered SET GPT_ASSESSMENT = ?, GPT_Score = ? WHERE rowid = ?", (assessment, score, id))
        conn.commit()
    except:
        traceback.print_exc()
        time.sleep(60)
        continue