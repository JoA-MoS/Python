class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.tax = .12
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self, template='Price: {}\r\nSpeed: {}mph\r\nFuel: {}\r\nMileage: {}mpg\r\nTax: {}'):
        print template.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        if self._price > 10000:
            self.tax = .15
        else:
            self.tax = .12


cars = [Car(2000, 35, 1, 15),
        Car(20000, 15, .8, 30),
        Car(1000, 25, .25, 15),
        Car(12345, 35, .75, 25),
        Car(2000, 35, 0, 15),
        Car(123, 35, .5, 15), ]
