""" Bike Object """


class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self._miles = miles

    def displayInfo(self):
        info_template = """price: {}\r\nmax speed: {}\r\nmiles:{}"""
        print info_template.format(self.price, self.max_speed, self.miles)
        return self

    def ride(self, miles=10):
        print 'Riding'
        self.miles += miles
        return self

    def reverse(self, miles=5):
        print 'Reversing'
        self.miles -= miles
        return self

    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, value):
        if value < 0:
            value = 0
        self._miles = value


my_bike = Bike(200, '25mph')
my_bike.ride().ride().ride().reverse().displayInfo()

my_bike2 = Bike(400, '25mph')
my_bike2.ride().ride().reverse().reverse().displayInfo()

my_bike3 = Bike(400, '25mph')
my_bike3.reverse().reverse().reverse().displayInfo()
