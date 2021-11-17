krotka3 = (1, 2, 3)
krotka4 = ("a", 4, "Python", 44.5, None, True)

# print(krotka4[0])
# print(krotka4.count(4))
# print(krotka4.index(None))

oceny = {1, 2, 5, 4, 3, 6, 3, 4, 1}
teksty = {"a", "c", "b", "d", "a", "b"}
tekst2 = {"k", "c", "b", "v", "h", "r"}
# print(oceny)
# print(teksty)
# print(tekst2.difference(teksty))
# print(tekst2 - teksty)
# print(teksty | tekst2)
# print(teksty.intersection(tekst2))
# print(teksty & tekst2)


# and  - odpowiednik &
# lub  - odpowiednik |


slownik = {"jeden": 1,
           "dwa": 2,
           "trzy": 3}

for key, value in slownik.items():
    print(key + " --> " + str(value))

print(slownik)
print(slownik["dwa"])
print(slownik.keys())
print(slownik.values())
# slownik["cztery"] = 4
# slownik[123] = "Tomek"
print(slownik)
print("dwa" in slownik.keys())

slownik2 = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
print(slownik2)

__ROK = 2021
print(__ROK)
