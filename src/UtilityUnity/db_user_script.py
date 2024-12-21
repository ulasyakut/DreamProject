import sqlite3
import csv

conn = sqlite3.connect('/Users/uyakut/Desktop/DreamProject/src/WebApp/data.sqlite')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    
    id INTEGER PRIMARY KEY NOT NULL,
    ssn TEXT UNIQUE NOT NULL,             
    name TEXT NOT NULL,
    zipcode TEXT,
    dob TEXT
)
''')

with open('citizen_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO users (id,ssn, name, zipcode, dob)
        VALUES (:account_id, :ssn, :name, :zipcode,  :dob)
        ''', row)


conn.commit()
conn.close()
