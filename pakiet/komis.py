from abc import ABC, abstractmethod


class jednoslad(ABC):
    wlasciciel = "MotoArt sp zoo"
    przebieg = 0

    def __init__(self, typ, marka, kolor):
        self.typ = typ
        self.marka = marka
        self.kolor = kolor

    def jedz(self):
        self.przebieg += 1

    def podajPrzebieg(self):
        return self.przebieg

    @abstractmethod
    def podajDane(self):
        pass


class motocykl(jednoslad):
    def __init__(self, marka, kolor, rocznik, predkoscMax):
        super().__init__("motocykl", marka, kolor)
        self.rocznik = rocznik
        self.predkoscMax = predkoscMax

    def podajDane(self):
        dane = "Ścigacz "+ str(self.predkoscMax) +" max km/h"+"\n"
        dane += "Marki " + self.marka +"\n"
        dane += "Przebieg " + str(self.podajPrzebieg()) +"\n"
        return dane

class skuter(jednoslad):
    def __init__(self, marka, kolor, rocznik, styl):
        super().__init__("skuter", marka, kolor)
        self.styl = styl
        self.skrzynia = "automat"

    def podajDane(self):
        dane = "Stylowy skuter " + self.styl + "\n"
        dane += "Marki " + self.marka + "\n"
        dane += "Przebieg " + str(self.podajPrzebieg()) + "\n"
        return dane


