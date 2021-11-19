from pakiet.menu import *
from pakiet.klasa import *

if __name__ == "__main__":
    # menu()
    adam = Czlowiek("Adam", 28, "mężczyzna")
    print("Kopia klasy Człowiek = ", adam.imie, adam.wiek, adam.plec)
    adam.przywitaj()
    adam.ruszaj()
    adam.mysl()

    ewa = Czlowiek("Ewa", 28, 'kobieta')
    print("Kopia klasy Człowiek = ", ewa.imie, ewa.wiek, ewa.plec)
    ewa.przywitaj()
    ewa.ruszaj()
    ewa.mysl()

    ufo = Czlowiek(imie="E.T.", plec='mężczyzna')
    print("Kopia klasy Człowiek = ", ufo.imie, ufo.wiek, ufo.plec)
