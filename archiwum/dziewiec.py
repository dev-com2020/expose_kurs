import random


def wydruk():
    imie = input("Podaj imię:")
    print("Hej", imie, "Wydrukowałem!")


# print("To jest zwykły print")
#
# lista = ["0", "1", "2"]
# menu = random.choice(lista)
menu = input("""
**********************
Witaj w moim programie
**********************
Wybierz z menu:
0,1 lub 2
""")
if menu == "0":
    print("Nic nie robie...")
elif menu == "1":
    print("Brzydka dziś pogoda...")
elif menu == "2":
    wydruk()

