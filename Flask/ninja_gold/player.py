# from session_helper import SessionHelper
import json
from collections import namedtuple
from flask import session


class Player(object):
    def __init__(self, name='Ninja', gold=0, *args, **kwargs):
        print
        self.name = name
        self.gold = gold

    @classmethod
    def newFromJson(cls, jsonStr):
        temp = cls()
        temp = json.loads(jsonStr, object_hook=lambda d: namedtuple(
            'X', d.keys())(*d.values()))
        return temp

    # I wanted load and Save in another class but could not get them implemented generically
    def loadJson(self, jsonStr):
        self = json.loads(jsonStr, object_hook=lambda d: namedtuple(
            'X', d.keys())(*d.values()))
        print self.name
        print self.gold
        return self

    # Save to Session
    def toJson(self):
        return json.dumps(self.__dict__)
