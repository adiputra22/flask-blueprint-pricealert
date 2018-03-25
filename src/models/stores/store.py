class Store(object):
    def __init__(self, name, url_prefix):
        self.name = name
        self.url_prefix = url_prefix

    def __repr__(self):
        return "<Store {} with url prefix {}>".format(self.name, self.url_prefix)