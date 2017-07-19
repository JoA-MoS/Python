from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

IMAGE_FOLDER = 'images'

NINJA_IMAGES = {'all': 'tmnt.png',
                'purple': 'donatello.jpg',
                'blue': 'leonardo.jpg',
                'orange': 'michelangelo.jpg',
                'red': 'raphael.jpg',
                '404': 'notapril.jpg', }


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/ninjas')
@app.route('/ninjas/<color>')
def ninjas(color=None):

    if color is None:
        ninja_image = url_for('static', filename=IMAGE_FOLDER +
                              '/' + NINJA_IMAGES['all'])
    elif color not in NINJA_IMAGES:
        ninja_image = url_for('static', filename=IMAGE_FOLDER +
                              '/' + NINJA_IMAGES['404'])

    else:
        ninja_image = url_for('static', filename=IMAGE_FOLDER +
                              '/' + NINJA_IMAGES[color])

    return render_template('/ninjas.html', image=ninja_image)


app.run(debug=True)
