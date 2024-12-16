import sqlite3
import csv


conn = sqlite3.connect('company.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS bills (
    account_number INTEGER PRIMARY KEY,
    amount INTEGER,             
    status TEXT,
    due_date TEXT,
    category TEXT
)
''')

with open('bills.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        try:
            
            cursor.execute('''
            INSERT INTO bills (account_number, amount, status, due_date, category)
            VALUES (:account_number, :amount, :status, :due_date, :category)
            ''', row)
        except sqlite3.IntegrityError:
            print(f"Duplicate account_number found: {row['account_number']}. Skipping row.")


conn.commit()
conn.close()
