
import sqlite3
from datetime import datetime

DB_NAME = "chat_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT,
            timestamp TEXT
        )
        '''
    )

    conn.commit()
    conn.close()

init_db()

def log_chat(user_message: str, bot_response: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO chat_logs (user_message, bot_response, timestamp)
        VALUES (?, ?, ?)
        ''',
        (user_message, bot_response, str(datetime.now()))
    )

    conn.commit()
    conn.close()
