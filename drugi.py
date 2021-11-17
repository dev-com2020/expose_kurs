# imie = "Tomasz"
# nazwisko = "Kowalski"
#
# print(imie[0])
# print(imie[-1])
# print(imie[0] + imie[-1] + imie[2:5])
# print(nazwisko[3:])
# # nazwisko[0] = "G" #tak się nie da!
#
# print(imie.count("a"))
# print(nazwisko.count("k"))
# print("Szkolenie".count("z"))
# print(imie.upper())
# print(imie.lower())
# print(len(nazwisko))

# jezyk_programowania = str(input("Podaj nazwę języka progr.:"))
# jezyk2 = str(input("Podaj nazwę drugiego języka progr.:"))
# slowo = "Lubię %s oraz %sa" % (jezyk_programowania, jezyk2)
# print(slowo)

#   %s - ciąg znakowy
#   %i - liczba całkowita int
#   %f - liczba zmiennoprzec. float
#   %x lub %X - liczba całkowita zapisana w formie szesntastkowej

print("Posiadam wersję Python: %i" % 3)
print("A dokładniej: %f" % 3.8)
print("A dokładniej: %.1f" % 3.8)
print("A dokładniej: %.f" % 3.8)
print("w systemie szesnastkowym: %X" % 4)

print("Lubię %(jezyk)s" % {"jezyk":"Pythona"})

print("Lubię język {1} oraz {0}".format("Java","Python"))