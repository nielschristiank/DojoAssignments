from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Z][a-zA-Z.-]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.-_]+$')
PW_REGEX = re.compile(r'^.{8,}$') #[a-zA-Z0-9.+_-]
app = Flask(__name__)
app.secret_key = 'KEKFHDSKDJFHDJDHSDJKSDJKHDKJSDKBJFDSJKBSDJLHBSDLHJBSDLHJB'
mysql = MySQLConnector(app,'the_wall')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall')
def wall():
    messages_query = """SELECT messages.id, message, messages.created_at, messages.updated_at, messages.user_id, users.username
                        FROM messages JOIN users ON users.id = messages.user_id
                        ORDER BY messages.created_at DESC"""
    comments_query = """SELECT comments.id, comment, comments.created_at, comments.updated_at, comments.message_id, messages.id as message_match_id, users.username
                        FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON users.id = comments.user_id
                        ORDER BY comments.created_at ASC"""
    messages = mysql.query_db(messages_query)
    comments = mysql.query_db(comments_query)
    # messages = mysql.query_db("SELECT messages.id, message, messages.created_at, messages.updated_at, users.username FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC")
    # comments = mysql.query_db("SELECT comments.id, comment, comments.created_at, comments.updated_at, comments.message_id, messages.id as message_match_id, users.username FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON users.id = comments.user_id ORDER BY comments.created_at ASC")
    return render_template('wall.html', all_messages=messages, all_comments=comments)

@app.route('/create_user', methods=['POST'])
def create_user():
    # found_user_query = mysql.query_db("SELECT username FROM users WHERE users.username = :username")
    # found_user_data = {'username':request.form['username']}
    # found_user = mysql.query_db(found_user_query, found_user_data)
    #
    # found_email_query = mysql.query_db("SELECT email FROM users WHERE users.email = :email")
    # found_email_data = {'email': request.form['email']}
    # found_email = mysql.query_db(found_user_query, found_user_data)

    validated = True

    if not USERNAME_REGEX.match(request.form['username']):
        flash('Invalid Username: can only include a-z, A-Z, 0-9, _, or -','reg_errors')
        validated = False
    if not NAME_REGEX.match(request.form['first_name']):
        flash('First Name Invalid: must be minimum of 2 characters, and start with a capital letter','reg_errors')
        validated = False
    if not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name Invalid: must be minimum of 2 characters, and start with a capital letter','reg_errors')
        validated = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email is Invalid','reg_errors')
        validated = False
    if not PW_REGEX.match(request.form['password']):
        flash('password must be minimum of 8 characters','reg_errors')
        validated = False
    if request.form['passwordconf'] != request.form['password']:
        flash('passwords must match','reg_errors')
        validated = False

    if validated == False:
        return redirect('/')
    else:
        found_user_query = "SELECT email, username FROM users WHERE users.email = :email OR users.username = :username"
        found_user_data = {'email': request.form['email'], 'username':request.form['username']}
        found_users = mysql.query_db(found_user_query, found_user_data)
        for found_user in found_users:
            if found_user['username'] == request.form['username']:
                flash("Username already exists", 'reg_errors')
                validated = False
            if found_user['email'] == request.form['email']:
                flash("Email already exists", 'reg_errors')
                validated = False

        if validated == False:
            return redirect ('/')
        else:
            salt = binascii.b2a_hex(os.urandom(15))
            hashword = md5.new(request.form['password'] + salt).hexdigest()
            query = "INSERT INTO users (username, first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:u_name, :f_name, :l_name, :email, :password, :salt, NOW(), NOW())"
            data = {'u_name': request.form['username'], 'f_name': request.form['first_name'], 'l_name': request.form['last_name'], 'email': request.form['email'], 'password': hashword, 'salt': salt}
            mysql.query_db(query, data)
            user_query = "SELECT * FROM users WHERE users.username = :u_name LIMIT 1"
            user_data = {'u_name': request.form['username']}
            user = mysql.query_db(user_query, user_data)
            session['user'] = {
            'id':user[0]['id'],
            'username':user[0]['username'],
            'first_name':user[0]['first_name'],
            'last_name':user[0]['last_name'],
            'email':user[0]['email']
            }
            return redirect('/wall')

    return redirect('/')

    # users = mysql.query_db("SELECT * FROM users")
    #
    # validated = True
    #
    # for user in users:
    #     if user['username'] == request.form['username']:
    #         flash("Username already exists", 'reg_errors')
    #         validated = False
    # if not USERNAME_REGEX.match(request.form['username']):
    #     flash('Invalid Username: can only include a-z, A-Z, 0-9, _, or -','reg_errors')
    #     validated = False
    # if not NAME_REGEX.match(request.form['first_name']):
    #     flash('First Name Invalid: must be minimum of 2 characters, and start with a capital letter','reg_errors')
    #     validated = False
    # if not NAME_REGEX.match(request.form['last_name']):
    #     flash('Last Name Invalid: must be minimum of 2 characters, and start with a capital letter','reg_errors')
    #     validated = False
    # if not EMAIL_REGEX.match(request.form['email']):
    #     flash('Email is Invalid','reg_errors')
    #     validated = False
    # for user in users:
    #     if user['email'] == request.form['email']:
    #         flash("Email already exists", 'reg_errors')
    #         validated = False
    # if not PW_REGEX.match(request.form['password']):
    #     flash('password must be minimum of 8 characters','reg_errors')
    #     validated = False
    # if request.form['passwordconf'] != request.form['password']:
    #     flash('passwords must match','reg_errors')
    #         validated = False

    # if validated == True:
    #     salt = binascii.b2a_hex(os.urandom(15))
    #     hashword = md5.new(request.form['password'] + salt).hexdigest()
    #     query = "INSERT INTO users (username, first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:u_name, :f_name, :l_name, :email, :password, :salt, NOW(), NOW())"
    #     data = {'u_name': request.form['username'], 'f_name': request.form['first_name'], 'l_name': request.form['last_name'], 'email': request.form['email'], 'password': hashword, 'salt': salt}
    #     mysql.query_db(query, data)
    #     user_query = "SELECT * FROM users WHERE users.username = :u_name LIMIT 1"
    #     user_data = {'u_name': request.form['username']}
    #     user = mysql.query_db(user_query, user_data)
    #     session['user'] = {
    #     'id':user[0]['id'],
    #     'username':user[0]['username'],
    #     'first_name':user[0]['first_name'],
    #     'last_name':user[0]['last_name'],
    #     'email':user[0]['email']
    #     }
    #     return redirect('/wall')

    # return redirect('/')

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
            session['user'] = {
            'id':user[0]['id'],
            'username':user[0]['username'],
            'first_name':user[0]['first_name'],
            'last_name':user[0]['last_name'],
            'email':user[0]['email']
            }
            return redirect('/wall')
        else:
            flash('Invalid password', 'login_errors')
    else:
        flash('Invalid username', 'login_errors')

    return redirect('/')

@app.route('/post_message', methods=['POST'])
def post_message():
    msg_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    msg_data = {
        'user_id':session['user']['id'],
        'message':request.form['message']
    }
    mysql.query_db(msg_query, msg_data)
    return redirect('/wall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def post_comment(message_id):
    com_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    com_data = {
        'user_id':session['user']['id'],
        'message_id': message_id,
        'comment':request.form['comment']
    }
    mysql.query_db(com_query, com_data)
    return redirect('/wall')

@app.route('/delete_message/<message_id>', methods=['POST'])
def delete_message(message_id):
    del_query = "DELETE FROM messages WHERE messages.id = :message_id"
    del_data = {'message_id': message_id}
    mysql.query_db(del_query, del_data)
    return redirect('/wall')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
