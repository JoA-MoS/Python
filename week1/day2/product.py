class Statuses(object):
    FOR_SALE = 1
    SOLD = 0
    DEFECTIVE = -1


class Reasons(object):
    DEFECTIVE = -1
    OPEN_BOX = 0
    LIKE_NEW = 1


class Product(object):
    def __init__(self, price, name, weight, brand, cost, status=Statuses.FOR_SALE):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = Statuses.SOLD
        return self

    def add_tax(self, tax_rate):
        return self.price * (1 + tax_rate)

    def return_product(self, reason):
        if reason == Reasons.DEFECTIVE:
            self.price = 0
            self.status = Statuses.DEFECTIVE
        elif reason == Reasons.OPEN_BOX:
            self.price *= .80
            self.status = Statuses.FOR_SALE
        else:
            self.status = Statuses.FOR_SALE
        return self

    def display_info(self, template='Price: {}\r\nName: {}\r\nWeight: {}\r\nBrand: {}\r\nCost: {}\r\nStatus: {}'):
        print template.format(self.price, self.name, self.weight, self.brand, self.cost, self.status)
        return self


products = [Product(100, 'Sun Glasses', '1', 'Oakley', 50)]

products[0].display_info()
print products[0].add_tax(.10)

products[0].sell().display_info()
products[0].return_product(Reasons.LIKE_NEW).display_info()
products[0].return_product(Reasons.OPEN_BOX).display_info()
products[0].return_product(Reasons.DEFECTIVE).display_info()
