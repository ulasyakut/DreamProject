import sqlite3

conn = sqlite3.connect('company.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS beneficiary (
    beneficiary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    name TEXT,             
    ssn TEXT,
    zipcode TEXT,
    dob TEXT,
    FOREIGN KEY (account_id) REFERENCES users(account_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS verified_bills (
    verified_bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    beneficiary_id INTEGER,             
    amount REAL,
    status TEXT,
    due_date TEXT,
    category TEXT,
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiary(beneficiary_id)
    FOREIGN KEY (bill_id) REFERENCES bills(bill_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transaction_history (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    verified_bill_id INTEGER,
    donor_name TEXT,             
    FOREIGN KEY (verified_bill_id) REFERENCES verified_bills(verified_bill_id)
)
''')


conn.commit()
conn.close()