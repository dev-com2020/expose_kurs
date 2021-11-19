class Czlowiek:

    def __init__(self, imie="Nieznany", wiek=0, plec='kobieta'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Cześć, mam na imię:", self.imie)

    def ruszaj(self):
        if self.plec == 'kobieta':
            print("Ruszyłam w drogę!")
        else:
            print("Ruszyłem w drogę!")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się uczę!")
        else:
            print("2+2*5/4")
