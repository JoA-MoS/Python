class Building(object):
    def __init__(self, name, min_gold, max_gold):
        self.name = name
        self.min_gold = min_gold
        self.max_gold = max_gold


class Buildings(list):
    def find(self, cb):
        return next((x for x in self if cb(x)), None)

    def getByName(self, name):
        return self.find(lambda x: x.name.lower()==name)

    