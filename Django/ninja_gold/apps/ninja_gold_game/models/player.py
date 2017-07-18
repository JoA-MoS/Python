# from session_helper import SessionHelper
import pickle
from activity import Activity
import datetime
from dateutil.parser import *


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


class Player(object):
    def __init__(self, gold=0, activities=[]):
        # self.name = name
        self.gold = gold
        self.activities = activities

    # def __str__(self):
    #     return self.toJson()

    def append_activity(self, msg, amnt, ts=datetime.datetime.now()):
        self.activities.append(Activity(msg, amnt, ts))

    # Save to session
    def toSession(self, ses):
        # ses['p_name'] = self.name
        ses['p_gold'] = self.gold
        ses['p_activities'] = []
        for a in self.activities:
            ses['p_activities'].append(
                (a.message, a.amount, date_handler(a.time_stamp), a.color))

        return self

    def loadSession(self, ses):
        # self.name = ses['p_name'] or 'Player1'
        if 'p_gold' in ses:
            self.gold = ses['p_gold']
        else:
            self.gold = 0

        self.activities = []
        if 'p_activities' in ses:
            for a in ses['p_activities']:
                self.append_activity(a[0], a[1], parse(a[2]))
        return self

    # @classmethod
    # def newFromJson(cls, jsonStr):
    #     temp = cls()
    #     temp = json.loads(jsonStr, object_hook=lambda d: namedtuple(
    #         'X', d.keys())(*d.values()))
    #     return temp

    # I wanted load and Save in another class but could not get them implemented generically
    # def loadJson(self, jsonStr):
    #     # self = json.loads(jsonStr, object_hook=lambda d: namedtuple(
    #     #     'X', d.keys())(*d.values()))
    #     print self.name
    #     print self.gold
    #     return self

    def toJson(self):
        return pickle.dumps(self)
