import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''create table entries (
  id INT AUTO_INCREMENT,
  title TEXT,
  content TEXT,
  posted_on DATETIME,
  primary key (id)
  )''')
cursor.close()
conn.close()