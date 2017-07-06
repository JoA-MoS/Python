class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return 'Species: {}\r\nName: {}\r\nHealth: {}'.format(type(self).__name__, self.name, self.health)

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health


class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a Dragon'


a = Animal('Ted')
a.walk().walk().walk().run().run().display_health()

d = Dog('Goldy')
d.walk().walk().walk().pet().pet().display_health()

dragon = Dragon('Toothless')

dragon.fly().walk().run().display_health()

print dragon
