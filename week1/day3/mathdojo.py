class MathDojo(object):
    def __init__(self, v=0):
        self.result = v

    def __str__(self):
        return str(self.result)

    def add(self, *args):
        for i in args:
            if type(i) is int or type(i) is float:
                self.result += i
            else:
                self.result += sum(i)
        return self

    def subtract(self, *args):
        for i in args:
            if type(i) is int or type(i) is float:
                self.result -= i
            else:
                self.result -= sum(i)
        return self


# md = MathDojo(0)

# print md.add(2).add(2, 5).subtract(3, 2).result
# print md


md2 = MathDojo()
print md2.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3])
