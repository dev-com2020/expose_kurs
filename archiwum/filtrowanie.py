def filtr(x):
    return x % 2 != 0 and x % 3 != 0

def szescian(x):
    return x * x * x

pierwsze = list(map(szescian, range(1,15)))

print("Liczby:", pierwsze)

