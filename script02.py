class dogo:
    def __init__(self, counter):
        self.counter = counter

    def raise_counter(self):
          self.counter += 1


def math(x, y):
    dogo_1 = dogo(x)

    while dogo_1.counter != y:
        dogo_1.raise_counter()
        print(dogo_1.counter)

math(21,37)