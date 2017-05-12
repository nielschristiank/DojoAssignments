from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit_form():
    name = request.form['name']
    favDCHero = request.form['favDCHero']
    favMarvelHero = request.form['favMarvelHero']
    comment = request.form['comment']
    print name, favDCHero, favMarvelHero, comment
    return render_template('result.html', name=name, favDCHero=favDCHero, favMarvelHero=favMarvelHero, comment=comment)

app.run(debug=True)
