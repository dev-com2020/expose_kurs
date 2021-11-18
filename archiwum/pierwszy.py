import random

dice = random.randint(1, 6)

print('Wynik rzutu:', dice)

# print("\tCześć, jestem Tomek\nCześć, jestem Tomek\nCześć, jestem Tomek\nCześć, jestem Tomek")

print('''
    Cześć, jestem Tomek
        Cześć, jestem Tomek
            Cześć, jestem Tomek
''')

print('"1+2-4*4/3.0"')
print("* " * 10)
print("Szkoleni" + "e")

liczba1 = 1
liczba2 = 2

# print(liczba1 > liczba2)
# print(liczba1 <= liczba2)
# print(liczba1 == liczba2)
# print(liczba1 != liczba2)

prawda = True
falsz = False

print(not not prawda)

calkowita = 3  # int
rzeczywista = 3.33  # float

cyfra = int(input("Podaj liczbę 1: "))
cyfra2 = input("Podaj liczbę 2: ")
print("Wynik=", cyfra + int(cyfra2))
print(type(cyfra))

# imie = input("Jak masz na imię?")
# print("Hej", imie)

a, b, c = 3, 4, 6

