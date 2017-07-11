from flask import Flask, render_template, redirect
import json
from building import Building, Buildings
from player import Player
from random import randint, randrange

app = Flask(__name__)

PLAYER = Player()

BUILDINGS = Buildings()
BUILDINGS.extend([Building('Farm', 10, 20),
                    Building('Cave', 5, 10),
                    Building('House', 2, 5),
                    Building('Casino', -50, 50), ])


@app.route('/')
def default():
    print json.dumps(PLAYER.__dict__)
    print json.dumps([b.__dict__ for b in BUILDINGS])
    return render_template('/index.html', buildings=BUILDINGS, player=PLAYER)


@app.route('/process_money/<building>', methods=['POST'])
def process_money(building):
    max_gold = BUILDINGS.getByName(building).max_gold
    min_gold = BUILDINGS.getByName(building).min_gold
    print str(min_gold) + ' - ' + str(max_gold)
    cur_gold = randint(min_gold, max_gold)
    print cur_gold

    return redirect('/')


app.run(debug=True)
