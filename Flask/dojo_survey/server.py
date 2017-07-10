from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def survey():
    return render_template('/survey.html')


@app.route('/result', methods=['POST'])
def result():
    for i in request.form:
        print i + ' - ' + request.form[i]
    return render_template('/result.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])


app.run(debug=True)
