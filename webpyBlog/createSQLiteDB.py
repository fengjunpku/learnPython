import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''create table entries (
  id INTEGER PRIMARY KEY NOT NULL,
  title TEXT,
  content TEXT,
  posted_on DATETIME
  )''')
cursor.close()
conn.close()