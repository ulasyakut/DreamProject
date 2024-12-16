import sqlite3
import csv

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    
    account_number INTEGER PRIMARY KEY,
    ssn INTEGER UNIQUE,             
    name TEXT,
    zipcode INTEGER,
    dob TEXT
)
''')

with open('citizen_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO users (account_number, ssn, name, zipcode, dob)
        VALUES ( :account_number,:ssn, :name, :zipcode,  :dob)
        ''', row)


conn.commit()
conn.close()
