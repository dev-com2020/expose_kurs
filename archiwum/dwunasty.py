def robie_duzo_rzeczy(*args, **kwargs):
    print(args)
    print(kwargs)


# robie_duzo_rzeczy(5, "Tomek", True, 8.56, imie="Tomek", wiek=38, wzrost=176)

a = 5
print(a)

def mam_global():
    global a
    a = 1
    b = 2
    d = a + b
    return d

def nie_mam_globala():
    c = 3
    return a + c

print(mam_global())
print(nie_mam_globala())
print(a)

