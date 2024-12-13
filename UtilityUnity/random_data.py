from faker import Faker
import csv
import pandas as pd

fake = Faker()

name = []
ssn = []
zipcode = []
account_number =[]
dob = []


for _ in range(30):
    ssn.append(fake.ssn())

for _ in range(30):
    name.append(fake.name())

for _ in range(10):
    zipcode.append(fake.zipcode_in_state(state_abbr='DE'))
    zipcode.append(fake.zipcode_in_state(state_abbr='PA'))
    zipcode.append(fake.zipcode_in_state(state_abbr='MD'))

for _ in range(30):
    account_number.append(fake.aba())

for _ in range(30):
    dob.append(fake.date_of_birth(minimum_age=18, maximum_age=100))




persons = []
for i in range(30):
    person = {}
    person['ssn'] = ssn[i]
    person['name'] = name[i]
    person['zipcode'] = zipcode[i]
    person['account number'] = account_number[i]
    person['dob'] = dob[i]
    persons.append(person)


df = pd.DataFrame(persons)
df.to_csv('citizen_data.csv',index=False)  
