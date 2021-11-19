import pandas as pd


def funckja(a, b):
    return a + b


print(funckja(3, 4))
zmienna = lambda a, b: a + b
print(zmienna(3, 4))

x = {"Imie": ["Michał", "Jakub", "Joanna"], "Płeć": ["M", "M", "K"]}
df = pd.DataFrame(x)


def zamien(x):
    if x == "M":
        return "Mężczyzna"
    else:
        return "Kobieta"


ww = df["Płeć"].apply(zamien)
# df = df["Płeć"].apply(lambda p: "Mężczyzna" if p == "M" else "Kobieta")
print(ww)
