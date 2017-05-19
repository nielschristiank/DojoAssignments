from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "iAmSecret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/two')#, methods=['GET'])
def clickTwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset') #, methods=['GET'])
def reset():
    session.pop('counter')
    return redirect('/')


app.run(debug=True)
