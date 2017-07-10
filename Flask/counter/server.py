from flask import Flask, session, render_template, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html', count=session['count'])


@app.route('/count/add/<val>')
def add(val):
    val = int(val)
    if 'count' in session:
        session['count'] += val
    else:
        session['count'] = val
    return redirect('/')


@app.route('/count/reset')
def reset():

    session['count'] = 0
    return render_template('index.html', count=session['count'])


app.run(debug=True)
