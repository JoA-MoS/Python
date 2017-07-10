from flask import Flask, request, redirect, render_template, session
from random import randint

app = Flask(__name__)
app.secret_key = '123456789'


@app.route('/')
def display():

    if 'number' not in session or 'hint' not in session:
        session['hint'] = 'I am thinking of a number between 1 and 100 take a guess!'
        session['number'] = randint(0, 101)
    else:
        hint = session['hint']

    return render_template('/index.html', text=hint, )


@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) > int(session['number']):
        session['hint'] = 'To High'
        session['state'] = 'high'
    if int(request.form['guess']) < int(session['number']):
        session['hint'] = 'To Low'
        session['state'] = 'low'
    if int(request.form['guess']) == int(session['number']):
        session['hint'] = 'You Got It! {} was the number'.format(
            session['number'])
        session['state'] = 'correct'
    return redirect('/')


app.run(debug=True)
