import sqlite3

conn = sqlite3.connect('tracker.db')
c = conn.cursor()
c.execute('SELECT * FROM ig_data')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
