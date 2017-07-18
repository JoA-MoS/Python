# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from models.building import Building, Buildings
from models.player import Player
from apps import NinjaGoldGameConfig

# Create your views here.
BUILDINGS = Buildings()
BUILDINGS.extend([Building('Farm', 10, 20),
                  Building('Cave', 5, 10),
                  Building('House', 2, 5),
                  Building('Casino', -50, 50),
                  Building('Dungenon', -1000, 1000), ])


def index(request):
    p = Player()
    p.loadSession(request.session)
    context = {'buildings': BUILDINGS,
               'player': p}
    return render(request, 'ninja_gold_game/index.html', context)


@require_http_methods(['POST'])
def process_money(request, buildingName):
    # load player from session
    p = Player()
    p = p.loadSession(request.session)
    b = BUILDINGS.getByName(buildingName)
    earnings = b.getGold()
    p.gold += earnings
    p.append_activity('visited {} and got {} gold'.format(
        b.name, earnings), earnings)
    p.toSession(request.session)
    return redirect('/')


def reset(request):
    request.session.flush()
    print 'session flushed'
    return redirect('/')
