from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Z][a-zA-Z.-]+$')
PW_REGEX = re.compile(r'^.{8,}$') #[a-zA-Z0-9.+_-]
app = Flask(__name__)
app.secret_key = 'keepitsecretkeepitsafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    if not NAME_REGEX.match(request.form['first_name']):
        flash('First Name Invalid (Capitalize first letter, and do not leave blank)')
    if not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name Invalid (Capitalize first letter, and do not leave blank)')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email Not valid')
    if not PW_REGEX.match(request.form['password']):
        flash('password must be min 8 characters')
    if request.form['password'] != request.form['passwordconf']:
        flash('passwords must match')

    return redirect('/')

app.run(debug=True)
