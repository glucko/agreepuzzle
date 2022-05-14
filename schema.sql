DROP TABLE IF EXISTS users;
CREATE TABLE users
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         email CHAR(100) NOT NULL,
         name CHAR(50) NOT NULL
         );