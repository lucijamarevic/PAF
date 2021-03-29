import matplotlib.pyplot as plt
import numpy as np
import math
import calculus as clc 

def f1(x):
    return 5*x**3 + 2*x*x - 3*x + 4

def analitic_derivative_f1(a,b):
    xlista = []
    ylista = []
    x = a
    while x <= b:
        xlista.append(x)
        x += 0.1
    for x in xlista:
        y = 15*x*x + 4*x - 3
        ylista.append(y)
    return xlista,ylista

plt.scatter(clc.derivative(f1,-2,2,0.1,2)[0], clc.derivative(f1,-2,2,0.1,2)[1], s = 3, c = 'blue')
plt.scatter(clc.derivative(f1,-2,2,0.01,2)[0], clc.derivative(f1,-2,2,0.01,2)[1], s = 1, c = 'red')
plt.plot(analitic_derivative_f1(-2,2)[0],analitic_derivative_f1(-2,2)[1], c = 'yellow')
plt.show()

def f2(x):
    return 2*math.sin(2*x) + 3*math.cos(x)

def analitic_derivative_f2(a,b):
    xlista = []
    ylista = []
    x = a
    while x <= b:
        xlista.append(x)
        x += 0.01
    for x in xlista:
        y = 4*math.cos(2*x) - 3*math.sin(x)
        ylista.append(y)
    return xlista,ylista

plt.scatter(clc.derivative(f2,-2,2,0.1,2)[0], clc.derivative(f2,-2,2,0.1,2)[1], s = 3, c = 'blue')
plt.scatter(clc.derivative(f2,-2,2,0.01,2)[0], clc.derivative(f2,-2,2,0.01,2)[1], s = 1, c = 'red')
plt.plot(analitic_derivative_f2(-2,2)[0],analitic_derivative_f2(-2,2)[1], c = 'yellow')
plt.show()