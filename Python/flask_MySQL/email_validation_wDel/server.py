from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KEKFHDSKDJFHDJDHSDJKSDJKHDKJSDKBJFDSJKBSDJLHBSDLHJBSDLHJB'
mysql = MySQLConnector(app,'email_validation_db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def add_email():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid")
        return redirect('/')

    emails = mysql.query_db("SELECT * FROM emails")

    for email in emails:
        if email['email'] == request.form['email']:
            flash("Email already exists")
            return redirect('/')

    if EMAIL_REGEX.match(request.form['email']):
        query= "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template('success.html', all_emails=emails)

@app.route('/delete_email/<id>', methods=['POST'])
def del_email(id):
        query = "DELETE FROM emails WHERE emails.id = :id"
        data = {'id': id}
        mysql.query_db(query, data)
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template('success.html', all_emails=emails)



app.run(debug=True)
