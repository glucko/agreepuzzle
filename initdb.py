import sqlite3
conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS USERS
         (ID INT PRIMARY KEY NOT NULL,
         EMAIL CHAR(100) NOT NULL,
         NAME CHAR(50) NOT NULL);''')
print("Table created successfully");
conn.close()