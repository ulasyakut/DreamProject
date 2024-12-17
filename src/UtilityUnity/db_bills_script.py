import sqlite3
import csv


conn = sqlite3.connect('company.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    amount REAL,             
    status TEXT,
    due_date TEXT,
    category TEXT,
    FOREIGN KEY (account_id) REFERENCES users(account_id)
)
''')

with open('bills.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO bills (account_id, amount, status, due_date, category)
        VALUES (:account_id, :amount, :status, :due_date, :category)
        ''', row)
        

conn.commit()
conn.close()
