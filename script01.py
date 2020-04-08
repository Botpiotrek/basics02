class Dogo:
    def foo (self):
        print("Jestem w klasie nadrzędnej")


class DogoDago(Dogo):
    def foo (self):
        print("Jestem w podklasie")


class Liar(Dogo):
    pass

dogo_1, dogo_2 = Dogo(), Dogo()
dogo_3, dogo_4  = DogoDago(), DogoDago()
dogo_5, dogo_6 = Liar(), Liar()

dogos = [dogo_1, dogo_2, dogo_3, dogo_4, dogo_5, dogo_6]

for dogo in dogos:
        dogo.foo()
