from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

#now = datetime.now().date

app = Flask(__name__)
app.secret_key = "iAmSecret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0;
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def getMoney():
    if 'message' not in session:
        session['message'] = []

    if request.form['building'] == 'farm':
        randGold = random.randrange(10,20)
        session['counter'] += randGold
    if request.form['building'] == 'cave':
        randGold = random.randrange(5,10)
        session['counter'] += randGold
    if request.form['building'] == 'house':
        randGold = random.randrange(2,5)
        session['counter'] += randGold
    if request.form['building'] == 'casino':
        randGold = random.randrange(-50,50)
        session['counter'] += randGold

    if randGold < 0:
        msg = ("red", str("Entered "+request.form['building']+" and lost "+str(randGold)+" golds...Ouch... "+"("+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")))
    else:
        msg = ("green", str("Earned "+str(randGold)+" golds from the "+request.form['building']+"! "+"("+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")))

    session['message'].insert(0,msg)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
