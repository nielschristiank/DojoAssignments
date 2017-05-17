from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "iAmSecret"

@app.route('/')
def index():
    session['randomNum'] = random.randrange(1,10)
    print session['randomNum']
    return render_template('index.html', hide='hide')#, congrats="GO FOR IT!", r)

@app.route('/guess', methods=['POST'])
def makeGuess():
    guess = request.form['num_guess']
    try:
        guess = int(guess)
        print type(guess)
        if guess == session['randomNum']:
            return render_template('index.html', guess=guess, congrats="You did it", color='green', hide='')
        elif guess > session['randomNum'] and guess < 11:
            return render_template('index.html', guess=guess, congrats="Too High", color='red', hide='hide')
        elif guess < session['randomNum'] and guess > 0:
            return render_template('index.html', guess=guess, congrats="Too Low", color='red', hide='hide')
    except:
        return render_template('index.html', guess=guess, congrats="Type an actual number!", color='black', hide='hide')
@app.route('/reset', methods=['POST'])
def reset():
    session.pop('randomNum')
    return redirect('/')

app.run(debug=True)
#
# from flask import Flask, render_template, request, redirect, session
# import random
#
# app = Flask(__name__)
# app.secret_key = "iAmSecret"
#
# @app.route('/')
# def index():
#     session['randomNum'] = random.randrange(1,10)
#     print session['randomNum']
#     return render_template('index.html', reset_button='hide')#, congrats="GO FOR IT!", r)
#
# @app.route('/guess', methods=['POST'])
# def makeGuess():
#     guess = request.form['num_guess']
#     try:
#         guess = int(guess)
#         print type(guess)
#         if guess == session['randomNum']:
#             return render_template('index.html', guess=guess, congrats="You did it", color='green', reset_button='')
#         elif guess > session['randomNum'] and guess < 11:
#             return render_template('index.html', guess=guess, congrats="Too High", color='red', reset_button='hide')
#         elif guess < session['randomNum'] and guess > 0:
#             return render_template('index.html', guess=guess, congrats="Too Low", color='red', reset_button='hide')
#         else:
#             return render_template('index.html', guess=guess, congrats="Pick a number in the range dummy!", reset_button='hide')
#     except:
#         return render_template('index.html', guess=guess, congrats="Type an actual number!", reset_button='hide')
# @app.route('/reset', methods=['POST'])
# def reset():
#     session.pop('randomNum')
#     return redirect('/')
#
# app.run(debug=True)
