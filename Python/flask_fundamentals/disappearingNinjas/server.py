from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', ninja_name='TMNT', src='img/tmnt.png')

@app.route('/ninjas/<ninja>')
def displayNinja(ninja):
    print ninja
    color = ninja
    if ninja == 'blue':
        ninja = 'img/leonardo.jpg'
        name = 'Leonardo'
    elif ninja == 'orange':
        ninja = 'img/michelangelo.jpg'
        name = 'Michelangelo'
    elif ninja == 'red':
        ninja = 'img/raphael.jpg'
        name = 'Raphael'
    elif ninja == 'purple':
        ninja = 'img/donatello.jpg'
        name = 'Donatello'
    else:
        ninja = 'img/notapril.jpg'
        name = 'Not a Turtle'

    return render_template('ninjas.html', src=ninja, ninja_name=name, turtle_color=color)

app.run(debug=True)
