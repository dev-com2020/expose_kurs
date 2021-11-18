"""
1.Użytkownik wybiera czy obstawia reszkę, czy orła (literka r – reszka, literka o – orzeł)
2.Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje 'rzutu’, czyli losowego wyboru orzeł / reszka.
3.Komputer wyświetla wynik rzutu.
4.Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
5.Wyświetla wyniki
6.Wracamy do punktu 1.
"""

import random
import time

# początkowe wyniki

user = 0
computer = 0

while True:
    # wczytujemy wybór
    x = input("Wybierz (o)rzeł lub (r)eszka, lub (x) aby zakończyć\n")
    if x == 'x':
        break
    elif x == 'o':
        x = "orzeł"
    elif x == 'r':
        x = "reszka"
    else:
        print("Proszę dokonać prawidłowego wyboru!")

    # rzucamy monetą
    y = random.choice(["orzeł", "reszka"])

    # odliczamy...

    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)
    print("Wynik rzutu:", y)

    # sprawdzamy kto wygrał
    if x == y:
        user += 1
    else:
        computer += 1

    print("Wyniki:\nUżytkownik:", user, "\nKomputer:", computer)
