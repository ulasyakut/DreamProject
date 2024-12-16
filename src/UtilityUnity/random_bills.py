from faker import Faker
import csv
import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

fake = Faker()

df = pd.read_csv('citizen_data.csv')
df = df['account number']
account_series = pd.Series(df)


accounts = pd.Series([i for i in account_series])
bills = pd.Series(np.random.randint(75, 175, size=60))
random_accounts = np.random.choice(accounts, size=len(bills))
status = np.random.choice(['Paid', 'Unpaid'], size=len(bills))
due_dates = [(datetime.now() + timedelta(days=np.random.randint(1, 31))).date() for _ in range(len(bills))]
category = np.random.choice(['Heat', 'Electricity'], size=len(bills))
bill_data = pd.DataFrame({
    "account number": random_accounts,
    "amount": bills,
    "status": status,
    "due date": due_dates,
    "category": category
})

bill_data.to_csv('bills.csv',index=False)  
