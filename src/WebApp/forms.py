from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddUserForm(FlaskForm):

    name = StringField('Name of User: ')
    ssn = StringField('SSN of User: ')
    zipcode = StringField('Zip Code of User: ')
    dob = StringField('DOB of User(YYYY-MM-DD): ')
    submit = SubmitField('Add User')


class AddBillForm(FlaskForm):

    status = StringField('Statu of Bill: ')
    user_id = IntegerField('User ID of User: ')
    due_date = StringField('Due Data of Bill(YYYY-MM-DD): ')
    category = StringField('Category of Bill: ')
    amount = IntegerField('Amount of Bill: ')
    submit = SubmitField('Add User')