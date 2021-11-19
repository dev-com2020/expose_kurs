import numpy as np

a = np.array([1, 3, 5, 7])
# print(a)
b = np.arange(4)
# print(b)
# print(a+b)
c = np.arange(2, 10, 1)
# print(c)
# print(c**2)
d = np.linspace(0, 10, 6)
# print(d)
e = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
# print(e>3)
# print(e)
#f = np.zeros((2,3))
f = np.random.random((2,3))
# print(f)
print(a[2:])
print(c[:1])

for i in c.flat:
    print(i)

