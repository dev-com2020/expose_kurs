from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tu", self.gatunek, "Startuje i osiągnę prędkość:", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):

    def __init__(self, szybkosc):
        super().__init__("Orzeł", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, "Rozpocząłem polowanie!")

    def wydaj_odglos(self):
        print("Wrrrrrrr")


class Kura(Ptak):

    def __init__(self):
        super().__init__("Kura", 0)

    def znosJajka(self):
        print("Tu", self.gatunek, "Znoszę jajko!")

    def lec(self):
        print("Tu", self.gatunek, "Ja nie umiem latać :(")

    def wydaj_odglos(self):
        print("Kokokokok")
