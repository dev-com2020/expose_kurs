# lista4 = ["a", 4, "Python", 44.5, None, True]
#
# for i in lista4:
#     print(i)
#
# for index, wartosc in enumerate(lista4):
#     print(str(index) + " --> " + str(wartosc))

licznik = 0
stan = True

while stan:
    licznik += 1
    print(licznik)
    if licznik > 10:
        stan = False

lista = []

print("Podaj liczby całkowite\n, aby zakończyć wpisz 'stop'...")
while True:
    wejscie = input("Wpisz cyfrę:")
    if wejscie == 'stop':
        break
    elif wejscie == 0:
        continue
    lista.append(int(wejscie))
print("Twoja lista: ", lista)
