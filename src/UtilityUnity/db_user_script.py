import sqlite3
import csv

conn = sqlite3.connect('company.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    
    account_id INTEGER PRIMARY KEY NOT NULL,
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
        INSERT INTO users (account_id,ssn, name, zipcode, dob)
        VALUES (:account_id, :ssn, :name, :zipcode,  :dob)
        ''', row)


conn.commit()
conn.close()
