from building import Building
from player import Player


class Game(object):
    def __init__(self, buildings, player=Player(), *args, **kwargs):
        self.player = player
        self.buildings = buildings

    def getBuildingByName(self, name):
        return next((b for b in self.buildings if b.name == name), None)
