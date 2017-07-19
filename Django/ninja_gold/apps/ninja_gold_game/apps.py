# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from models.building import Building, Buildings


class NinjaGoldGameConfig(AppConfig):
    name = 'ninja_gold_game'
    # buildings = Buildings()
    # buildings.extend([Building('Farm', 10, 20),
    #                   Building('Cave', 5, 10),
    #                   Building('House', 2, 5),
    #                   Building('Casino', -50, 50), ])
