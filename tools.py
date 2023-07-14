#Function to read a CSV into SQLite
def read(file):
    import sqlite3
    import csv
    conn = sqlite3.connect('DataAnalysis/tweets.db')
    cursor = conn.cursor()
    cursor.execute
    with open('SubAnalysis/commentsn.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        #not sure how I feel about this and don't know where to put it
        conn.execute('''CREATE TABLE IF NOT EXISTS Comments (
            subreddit TEXT,
            id TEXT,
            submission_id TEXT,
            body TEXT,
            created_utc INTEGER,
            parent_id TEXT,
            permalink TEXT,
            sentiment TEXT
        )''')
        
        # CSV to SQLite
        for row in reader:
            conn.execute("INSERT INTO Comments (subreddit, id, submission_id, body, created_utc, parent_id, permalink, sentiment) VALUES (?,?,?,?,?,?,?)", row)

    conn.commit()
    conn.close()

# Time related functions
import time
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def sleep(self):
        time.sleep(4) 
