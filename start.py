from pakiet.menu import *
from pakiet.klasa import *
from pakiet.ptak import *
from pakiet.komis import *
from pakiet.auto import *

if __name__ == "__main__":

    audi = Samochod()
    audi.uruchom()
    #audi.__biegNastepny()
    audi.przyspiesz()
    #audi.__predkosc = 100
    #audi.__biegPoprzedni()
    audi.hamuj()
    audi.wylacz()
    #print(audi.__silnik)




    #
    # def zapis(plik):
    #     outfile = open(plik, 'a')
    #     outfile.write(lista)
    #     outfile.close()
    #
    #
    # bazaDanych = []
    # bazaDanych.append(motocykl("Honda", "czerwony", 2006, 230))
    # bazaDanych.append(motocykl("BMW", "czarny", 2010, 190))
    # bazaDanych.append(skuter("Vespa", "biały", 2001, "retro"))
    # bazaDanych.append(skuter("Romet", "zielony", 1999, "nowoczesny"))


    # for i in bazaDanych:
    #     print(i.podajDane())

    #
    # for i in bazaDanych:
    #     lista = i.podajDane()
    #     zapis("baza_motorów.csv")


    # ptak1 = Orzel(100)
    # ptak2 = Kura()
    #
    # ptak1.lec()
    # ptak1.poluj()
    # ptak1.wydaj_odglos()
    #
    # ptak2.znosJajka()
    # ptak2.lec()
    # ptak2.wydaj_odglos()

    # menu()
    # adam = Czlowiek("Adam", 28, "mężczyzna")
    # print("Kopia klasy Człowiek = ", adam.imie, adam.wiek, adam.plec)
    # adam.przywitaj()
    # adam.ruszaj()
    # adam.mysl()
    #
    # ewa = Czlowiek("Ewa", 28, 'kobieta')
    # print("Kopia klasy Człowiek = ", ewa.imie, ewa.wiek, ewa.plec)
    # ewa.przywitaj()
    # ewa.ruszaj()
    # ewa.mysl()
    #
    # ufo = Czlowiek(imie="E.T.", plec='mężczyzna')
    # print("Kopia klasy Człowiek = ", ufo.imie, ufo.wiek, ufo.plec)
