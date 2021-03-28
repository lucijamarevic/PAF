import matplotlib.pyplot as plt
import numpy as np
import math
import calculus as clc 

def f1(x):
    return 5*x**3 + 2*x*x - 3*x + 4

def analitic_derivative_f1(a,b):
    xevi_ = np.linspace(a,b, num = 100)
    analiticke_ = []
    for x in xevi_:
        d = 15*x*x + 4*x - 3
        analiticke_.append(d)
    return xevi_, analiticke_

def f2(x):
    return 2*math.sin(2*x)

def analitic_derivative_f2(a,b):
    _xevi_ = np.linspace(a,b, num = 100)
    _analiticke_ = []
    for x in _xevi_:
        d = 2*math.cos(2*x)
        _analiticke_.append(d)
    return _xevi_, _analiticke_

def graph(func,a,b,h):
    plt.title("Graf derivacije")
    plt.scatter(clc.three_step(func,a,b,h)[0],clc.three_step(func,a,b,h)[1], s = 5, c = 'blue')
    analitic_derivative_f1(a,b)
    plt.scatter(analitic_derivative_f1(a,b)[0],analitic_derivative_f1(a,b)[1], s = 5, c = 'green')
    plt.show()

clc.three_step(f1,-10,10,0.0001)
graph(f1,-5,5,0.1)

clc.three_step(f2,-5,5,0.0001)
clc.draw_graph(f2,-5,5,0.0001)
