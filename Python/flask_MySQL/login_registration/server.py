from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Z][a-zA-Z.-]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.-_]+$')
PW_REGEX = re.compile(r'^.{8,}$') #[a-zA-Z0-9.+_-]
app = Flask(__name__)
app.secret_key = 'KEKFHDSKDJFHDJDHSDJKSDJKHDKJSDKBJFDSJKBSDJLHBSDLHJBSDLHJB'
mysql = MySQLConnector(app,'login_registration')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    users = mysql.query_db("SELECT * FROM users")

    validated = True

    for user in users:
        if user['username'] == request.form['username']:
            flash("Username already exists")
            validated = False
    if not USERNAME_REGEX.match(request.form['username']):
        flash('Invalid Username: can only include a-z, A-Z, 0-9, _, or -')
        validated = False
    if not NAME_REGEX.match(request.form['first_name']):
        flash('First Name Invalid: must be minimum of 2 characters, and start with a capital letter')
        validated = False
    if not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name Invalid: must be minimum of 2 characters, and start with a capital letter')
        validated = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email is Invalid')
        validated = False
    if not PW_REGEX.match(request.form['password']):
        flash('password must be minimum of 8 characters')
        validated = False
    if request.form['passwordconf'] != request.form['password']:
        flash('passwords must match')
        validated = False

    # if USERNAME_REGEX.match(request.form['username']) and NAME_REGEX.match(request.form['first_name']) and NAME_REGEX.match(request.form['last_name']) and EMAIL_REGEX.match(request.form['email']) and (request.form['passwordconf'] == request.form['password']):
    if validated:
        salt = binascii.b2a_hex(os.urandom(15))
        hashword = md5.new(request.form['password'] + salt).hexdigest()
        query = "INSERT INTO users (username, first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:u_name, :f_name, :l_name, :email, :password, :salt, NOW(), NOW())"
        data = {'u_name': request.form['username'], 'f_name': request.form['first_name'], 'l_name': request.form['last_name'], 'email': request.form['email'], 'password': hashword, 'salt': salt}
        mysql.query_db(query, data)
        user_query = "SELECT * FROM users WHERE users.username = :u_name LIMIT 1"
        user_data = {'u_name': request.form['username']}
        user = mysql.query_db(user_query, user_data)
        session['user'] = user[0]
        return render_template('user.html')

    return redirect('/')

@app.route('/login', methods=['POST'])
def user_login():
    username = request.form['username']
    password = request.form['password'];
    query = "SELECT * FROM users WHERE users.username = :u_name LIMIT 1"
    data = {'u_name': username}
    user = mysql.query_db(query, data)
    if len(user) != 0:
        encrypted_pw = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_pw:
            session['user'] = user[0]
            return render_template('user.html')
        else:
            flash('Invalid password')
    else:
        flash('Invalid username')

    return redirect('/')
app.run(debug=True)
