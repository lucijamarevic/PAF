import matplotlib.pyplot as plt
import math
import calculus as clc 

def f1(x):
    return 5*x**3 + 2*x*x - 3*x + 4

def der_f1(x):
    return 15*x*x + 4*x - 3

xlista, ylista = clc.derivative(f1,-2,2,0.1,2)
x1_lista, y1_lista = clc.derivative(f1,-2,2,0.01,2)
ya_lista = []
for x in xlista:
    ya = der_f1(x)
    ya_lista.append(ya)

plt.plot(xlista, ya_lista, c = "gray", label = "analitic")
plt.scatter(xlista, ylista, s = 3, c = "red", label = "e = 0.1")
plt.scatter(x1_lista, y1_lista, s = 3, c = "orange", label = "e = 0.01")
plt.title("S two_step metodom")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.show()

def f2(x):
    return 2*math.sin(2*x) + 3*math.cos(x)

def der_f2(x):
    return 4*math.cos(2*x) - 3*math.sin(x)

xlista, ylista = clc.derivative(f2,-2,2,0.1)
x1_lista, y1_lista = clc.derivative(f2,-2,2,0.01)
ya_lista = []
for x in xlista:
    ya = der_f2(x)
    ya_lista.append(ya)

plt.plot(xlista, ya_lista, c = "gray", label = "analitic")
plt.scatter(xlista, ylista, s = 3, c = "red", label = "e = 0.1")
plt.scatter(x1_lista, y1_lista, s = 3, c = "orange", label = "e = 0.01")
plt.title("S three_step metodom")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.show()