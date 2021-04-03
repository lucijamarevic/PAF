import matplotlib.pyplot as plt
import math
import calculus as clc 

def f1(x):
    return 2*x*x - 3

def int_f1(x):
    return (2/3)*x**3 - 3*x

a = 0
b = 5
dn = 50
nlista = []
g_mede = []
d_mede = []
analitic = []
trapez = []

for i in range(1,20):
    nlista.append(dn*i)

for n in nlista:
    gornja, donja = clc.integrate_rectangle(f1,a,b,n)
    g_mede.append(gornja)
    d_mede.append(donja)
    integral_t = clc.integrate_trapeze(f1,a,b,n)
    trapez.append(integral_t)
    integral_a = int_f1(b) - int_f1(a)
    analitic.append(integral_a)

plt.scatter(nlista, g_mede, s = 2, c = "red", label = "gornje mede")
plt.scatter(nlista, d_mede, s = 2, c = "orange", label = "donje mede")
plt.scatter(nlista, trapez, s = 2, c = "green", label = "trapezna intgegracija")
plt.plot(nlista, analitic, label = "analiticki")
plt.xlabel("N steps")
plt.ylabel("integral")
plt.legend()
plt.show()

def f2(x):      #jos jedna funkcija radi dodatne provjere ispravnosti
    return x*math.sin(x)

def int_f2(x):
    return math.sin(x) - x*math.cos(x)

a = 0
b = 5
dn = 50
nlista = []
g_mede = []
d_mede = []
analitic = []
trapez = []

for i in range(1,20):
    nlista.append(dn*i)

for n in nlista:
    gornja, donja = clc.integrate_rectangle(f2,a,b,n)
    g_mede.append(gornja)
    d_mede.append(donja)
    integral_t = clc.integrate_trapeze(f2,a,b,n)
    trapez.append(integral_t)
    integral_a = int_f2(b) - int_f2(a)
    analitic.append(integral_a)

plt.scatter(nlista, g_mede, s = 2, c = "red", label = "gornje mede")
plt.scatter(nlista, d_mede, s = 2, c = "orange", label = "donje mede")
plt.scatter(nlista, trapez, s = 2, c = "green", label = "trapezna intgegracija")
plt.plot(nlista, analitic, label = "analiticki")
plt.xlabel("N steps")
plt.ylabel("integral")
plt.legend()
plt.show()