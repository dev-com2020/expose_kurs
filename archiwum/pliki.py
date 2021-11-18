# zapisywanie
def zapis(plik):
    outfile = open(plik, 'w')
    outfile.write(str(lista))
    outfile.close()


# odczyt
def odczyt(plik):
    infile = open(plik, 'r')
    with open(plik) as f:
        lista2 = eval(f.read())
        print(lista2)
        print("Suma wszystkich elementów:", sum(lista2))
    infile.close()


lista = [1, 2, 3, 4, 5, 6]
lista2 = []

wybor = input("Wybierz co chcesz zrobic: 1= zapis,2=odczyt")
if wybor == "1":
    plik = input("Podaj nazwę pliku:")
    zapis(plik)
else:
    plik = input("Podaj nazwę pliku:")
    odczyt(plik)








