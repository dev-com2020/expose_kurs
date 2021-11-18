def ksero(tekst="Uwaga-nie podano argumentu,błąd funkcji!", ile=1):
    print((tekst + " ") * ile)


w1 = ["Tomek", "Halina", "Python"]
wybor = int(input("Wybierz indeks z listy(0-2)"))

if wybor == 0:
    wynik = w1[0]
    print("Wybrałeś:", w1[0])
    w2 = input("Podaj ilość kopii...")
    if w2 == "":
        ksero(wynik)
    else:
        ksero(wynik, int(w2))
elif wybor == 1:
    wynik = w1[1]
    print("Wybrałeś:", w1[1])
    w2 = input("Podaj ilość kopii...")
    if w2 == "":
        ksero(wynik)
    else:
        ksero(wynik, int(w2))
elif wybor == 2:
    wynik = w1[2]
    print("Wybrałeś:", w1[2])
    w2 = input("Podaj ilość kopii...")
    if w2 == "":
        ksero(wynik)
    else:
        ksero(wynik, int(w2))
else:
    ksero()


