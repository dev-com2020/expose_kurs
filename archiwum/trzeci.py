lista = [7, 8, 99, 45, 2, 1]
lista2 = list()
lista3 = [1, 2, 3]
lista4 = ["a", 4, "Python", 44.5, None, True]
lista5 = [lista3, lista4]
# lista3.extend(lista4)
lista6 = lista3 + lista4
lista7 = ["Tomek", "Janek", "Halina"]

lista.sort()
print(lista)
lista.reverse()
print(lista)

lista7.sort()
print(lista7)
# lista7.reverse()
# print(lista7)
lista7.append("Zbyszek")
lista7[0] = "Michał"
lista7.insert(2, "Michał2")
lista7.pop(0)
lista7.clear()
print(lista7)


# print(lista4[3:5])
# print(lista3)
# print(lista6)
