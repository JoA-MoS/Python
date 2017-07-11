import json
from random import randint
from collections import namedtuple


class Building(object):
    def __init__(self, name, min_gold, max_gold):
        self.name = name
        self.min_gold = min_gold
        self.max_gold = max_gold

    def getGold(self):
        return randint(self.min_gold, self.max_gold)


class Buildings(list):
    def find(self, cb):
        return next((x for x in self if cb(x)), None)

    def getByName(self, name):
        return self.find(lambda x: x.name.lower() == name)

     # I wanted load and Save in another class but could not get them implemented generically
    def loadJson(self, jsonStr):
        self = json.loads(jsonStr, object_hook=lambda d: namedtuple(
            'X', d.keys())(*d.values()))
        return self

    # Save to Session
    def toJson(self):
        return json.dumps([b.__dict__ for b in self])
