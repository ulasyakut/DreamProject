import os
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(base_dir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    ssn = db.Column(db.Text)
    zipcode = db.Column(db.Text)
    dob = db.Column(db.Text)

    bills = db.relationship('Bill',backref='user',lazy='dynamic')


    def __init__(self,name,ssn,zipcode,dob):
        self.name = name
        self.ssn = ssn
        self.zipcode = zipcode
        self.dob = dob
        

class Bill(db.Model):

    __tablename__ = 'bills'

    id = db.Column(db.Integer,primary_key=True)
    status = db.Column(db.Text)
    account_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    due_date = db.Column(db.Text)
    category = db.Column(db.Text)
    amount = db.Column(db.Integer)

    def __init__(self,status,account_id,due_date,category,amount):
        self.status = status
        self.account_id = account_id
        self.due_date = due_date
        self.category = category
        self.amount = amount





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adduser',methods = ['GET','POST'])
def add_user():
    
    form = AddUserForm()
    if form.validate_on_submit():
        name = form.name.data
        ssn = form.ssn.data
        zipcode = form.zipcode.data
        dob = form.dob.data

        new_user = User(name,ssn,zipcode,dob)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('list_user'))

    return render_template('adduser.html',form=form)

@app.route('/listuser')
def list_user():
    
    users = User.query.all()
    return render_template('listuser.html',users=users)
    



if __name__ == '__main__':
    app.run(debug=True)