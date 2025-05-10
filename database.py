import sqlite3
from datetime import datetime

DB_PATH = 'tracker.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 建立粉絲數記錄表
    c.execute('''
        CREATE TABLE IF NOT EXISTS follower_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            followers INTEGER
        )
    ''')

    # 建立貼文互動表，每篇貼文以 shortcode 作為主鍵
    c.execute('''
        CREATE TABLE IF NOT EXISTS post_data (
            shortcode TEXT PRIMARY KEY,
            timestamp TEXT,
            likes INTEGER,
            comments INTEGER
        )
    ''')

    conn.commit()
    conn.close()


def insert_follower_data(followers):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO follower_data (timestamp, followers) VALUES (?, ?)', (now, followers))
    conn.commit()
    conn.close()


def insert_post_data(shortcode, likes, comments, timestamp):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO post_data (shortcode, timestamp, likes, comments)
        VALUES (?, ?, ?, ?)
    ''', (shortcode, timestamp, likes, comments))
    conn.commit()
    conn.close()


def fetch_follower_data():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT timestamp, followers FROM follower_data ORDER BY timestamp')
    rows = c.fetchall()
    conn.close()
    return rows


def fetch_post_data():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT shortcode, timestamp, likes, comments FROM post_data ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    return rows
