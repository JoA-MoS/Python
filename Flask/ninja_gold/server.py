from flask import Flask, render_template, redirect, session
from building import Building, Buildings
from player import Player


app = Flask(__name__)
app.secret_key = 'NinjaGold2'


BUILDINGS = Buildings()
BUILDINGS.extend([Building('Farm', 10, 20),
                  Building('Cave', 5, 10),
                  Building('House', 2, 5),
                  Building('Casino', -50, 50), ])


@app.route('/')
def default():
    if 'player' not in session:
        print 'creating player'
        temp = Player('Justin', 0)
        session['player'] = temp.toJson()
    else:
        print 'getting existing player'
        temp = Player.newFromJson(session['player'])
    print tuple(temp)
    return render_template('/index.html', buildings=BUILDINGS, player=temp)


@app.route('/process_money/<building>', methods=['POST'])
def process_money(building):
    print session['player']
    p = Player().loadJson(session['player'])
    print 'before building - ' + str(p.gold)
    earnings = BUILDINGS.getByName(building).getGold()

    print 'earnings - ' + str(earnings)

    p.gold = p.gold + earnings

    print 'after building - ' + str(p.gold)
    session['player'] = p.toJson()
    return redirect('/')


app.run(debug=True)
