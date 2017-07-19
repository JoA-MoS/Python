import datetime


class Activity(object):
    def __init__(self, msg, amnt, ts=datetime.datetime.now()):
        self.time_stamp = ts
        self.message = msg
        self.amount = amnt

    @property
    def color(self):
        if self.amount < 0:
            return 'red'
        else:
            return 'green'
