from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'keepitsecretkeepitsafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    if len(request.form['name']) < 1:
        flash("Name field must not be empty!")
    if len(request.form['comment']) > 120:
        flash("Comment cannot be longer the 120 characters!")
    else:
        name = request.form['name']
        favDCHero = request.form['favDCHero']
        favMarvelHero = request.form['favMarvelHero']
        comment = request.form['comment']
        print name, favDCHero, favMarvelHero, comment
        #return render_template('result.html', name=name, favDCHero=favDCHero, favMarvelHero=favMarvelHero, comment=comment)
    return redirect('/')

app.run(debug=True)
