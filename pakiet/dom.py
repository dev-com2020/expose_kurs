class Budynek:
    __iloscOsob = 0

    def weszla(self):
        self.__iloscOsob += 1

    def wyszla(self):
        self.__iloscOsob -= 1

    def czyPusty(self):
        if self.__iloscOsob > 0:
            return False
        else:
            return True

b1 = Budynek()
b1.weszla()
print(b1.czyPusty())
b1.wyszla()
print(b1.czyPusty())
