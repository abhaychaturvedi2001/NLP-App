from flask import Flask, render_template,request,redirect, session
from db import database
import api


app = Flask(__name__)

dbo = database()
@app.route('/')
def index():

    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html',massage ="reginstration sucessful kindly login")
    else:
        return render_template('register.html', massage = "email already exist")

    return name + " " + email+ " " + password
@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('useremail')
    password = request.form.get('userpassword')
    response = dbo.search(email,password)
    if response:


        return redirect('/profile')
    else:
        return render_template('login.html', massage = " incorrect email/password")

@app.route('/profile')
def profile():

        return render_template('/profile.html')



@app.route('/ner')
def ner():

        return render_template('ner.html')

@app.route("/perform_ner", methods = ['post'])
def peform_ner():

        text = request.form.get("ner_text")
        response = api.ner(text)
        print(response)
        return render_template('ner.html', response = response)






app.run(debug = True)
