def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def glowna():
    def wewn(a, b):
        return a * b

    x = wewn(2, 3)
    return x


def funk():
    def wewn2(a, b):
        return a * b

    return wewn2


# print(glowna())
# print(wykonaj(dodaj, 2, 3))
# print(wykonaj(odejmij, 7, 3))
# liczba = funk()
# print(liczba(3, 3))

def dekor(funkcja):
    def wew():
        print("Nazwa funkcji:",funkcja.__name__)
        return funkcja()
    return wew


@dekor
def zwykla(a, b, c):
    print("TO jest zwykła funkcja")
    print("Wynik=", a + b + c)

@dekor
def pomnoz(a, b):
    print("Wynik mnożenia=", a * b)

@dekor
def pierwsza():
    print("ja tu sobie działam...")

@dekor
def druga():
    print("a ja sobie też działam tutaj...")

pierwsza()
druga()
pierwsza()


#
# zwykla(1, 2, 3)
# pomnoz(3,4)
