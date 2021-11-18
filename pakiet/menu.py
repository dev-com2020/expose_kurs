import pyfiglet
from pakiet.kalkulator import *


def menu():
    while True:
        try:
            wybor = input("Podaj rodzaj działania:(+,-,/,*) lub 'x' aby zakończyć")
            if wybor == "+":
                a = int(input("Cyfra 1:"))
                b = int(input("Cyfra 2:"))
                print(dodaj(a, b))
            elif wybor == "x":
                print("Dziękujemy i zapraszamy ponownie!")
                break
            elif wybor == "-":
                a = int(input("Cyfra 1:"))
                b = int(input("Cyfra 2:"))
                print(odejmij(a, b))
            elif wybor == "/":
                a = int(input("Cyfra 1:"))
                b = int(input("Cyfra 2:"))
                print(podziel(a, b))
            elif wybor == "*":
                a = int(input("Cyfra 1:"))
                b = int(input("Cyfra 2:"))
                print(pomnoz(a, b))
        except ZeroDivisionError:
            print("Nastąpiło dzielenie przez 0")
        except ValueError:
            print("Niepoprawna wartość")
        finally:
            baner = pyfiglet.Figlet(font='drpepper')
            print(baner.renderText("Kup kalkulator!"))
