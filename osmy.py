# import random
#
# lista = []
#
# for i in range(10):
#
#     lista.append(random.randint(1, 100))
#
#
# print(lista)
# print(("Najmniejsza:", min(lista)))
# print(("Największa:", max(lista)))


# liczby = [i for i in range(1, 101)]  # list comprehension
liczby = list(range(1, 101))

print(liczby)
print("Suma wynosi: ", sum(liczby))
print("Średnia wartość wynosi: ", sum(liczby) / len(liczby))
