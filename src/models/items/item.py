class Item(object):
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __repr__(self):
        return "<Item {} with url {} and price {}>".format(self.name, self.url, self.price)