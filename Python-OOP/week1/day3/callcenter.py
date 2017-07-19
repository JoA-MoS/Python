import uuid
import datetime


class Call(object):
    def __init__(self, name, number, reason, time=datetime.datetime.now()):
        self.id = uuid.uuid4()
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def __str__(self):
        return ('ID: {}\r\nName: {}\r\nNumber: {}\r\nTime: {}\r\nReason: {}'
                .format(self.id, self.name, self.number, self.time, self.reason))

    def display(self):
        print self


class CallCenter(object):
    def __init__(self, calls=[]):
        self.calls = calls

    @property
    def queue(self):
        return len(self.calls)

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def info(self):
        for c in self.calls:
            print c
        print 'Queue Length: ' + str(self.queue)

    def getCallByNumber(self, number):
        for c in self.calls:
            if c.number == number:
                return c

    def removeCallByNumber(self, number):
        for c in self.calls:
            if c.number == number:
                self.calls.remove(c)
        return self

    def sortByCallTime(self):
        self.calls.sort(key=lambda x: x.time)
        return self


c1 = Call('Justin', '5092304274', 'Just Testing')

cc = CallCenter([Call('Justin', '5092304274', 'Just Testing', datetime.datetime(2017, 1, 12)),
                 Call('Justin', '1234567890', 'Just Testing'),
                 Call('Justin', '098', 'Just Testing'),
                 Call('Justin', '5092304274', 'Just Testing'),
                 Call('Justin', '5092304274', 'Just Testing', datetime.datetime(2016, 1, 12)), ])


cc.info()
cc.remove()
cc.info()
cc.add(c1)
cc.info()
print '========================'
print cc.getCallByNumber('098')
cc.removeCallByNumber('098')
cc.info()
print '========================'
cc.sortByCallTime()
cc.info()
