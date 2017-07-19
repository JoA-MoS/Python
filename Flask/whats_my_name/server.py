from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def get_name():
    return render_template('/index.html')


@app.route('/process', methods=['POST'])
def process_form():
    print request.form['name']
    return redirect('/')


app.run(debug=True)
