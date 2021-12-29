from abc import ABC
class product(ABC):
    name = None
    price = None
    inventory = None
    def __init__(self, n, p, i):
        self.name = n
        self.price = p
        self.inventory = i

class book(product):
    author = None
    def __init__(self, n, p, i, a):
        self.author = a
        product.__init__(self, n, p, i)

class cd(product):
    musician = None
    def __init__(self, n, p, i, m):
        self.musician = m
        product.__init__(self, n, p, i)

class game(product):
    console = None
    def __init__(self, n, p, i, c):
        self.console = c
        product.__init__(self, n, p, i)
