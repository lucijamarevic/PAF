import matplotlib.pyplot as plt
import numpy as np
import math

def three_step(func,x,h):
    return (func(x+h) - func(x-h)) / (2*h)

def two_step(func,x,h):
    return (func(x+h) - func(x)) / h

def derivative(func,a,b,h,m = 3):
    xlista = []
    ylista = []
    x = a
    while x <= b:
        xlista.append(x)
        x += h

    if m == 2:
        for x in xlista:
            d = two_step(func,x,h)
            ylista.append(d)
    else:
        for x in xlista:
            d = three_step(func,x,h)
            ylista.append(d)

    return xlista,ylista
        
def integrate_rectangle(func,a,b,n):
    xlista = []
    ylista = []
    delta_x = (b-a)/n
    x = a
    while x <= b:
        xlista.append(x)
        x += delta_x
    
    for x in xlista:
        del xlista[0]
        y = func(x)*delta_x
        ylista.append(y)

    gornja_meda = sum(ylista)

    for x in xlista:
        del xlista[-1]
        y = func(x)*delta_x
        ylista.append(y)