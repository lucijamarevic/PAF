import matplotlib.pyplot as plt
import numpy as np
import math

def derivative(func,x,h):
    return (func(x+h) - func(x-h)) / (2*h)

def three_step(func,a,b,h):
    derivacije = []
    xevi = np.linspace(a,b, num = 50)
    for x in xevi:
        d_po_dx = derivative(func,x,h)
        derivacije.append(d_po_dx)
    return xevi, derivacije

def draw_graph(func,a,b,h):
    plt.title("Graf derivacije")
    plt.scatter(three_step(func,a,b,h)[0],three_step(func,a,b,h)[1], s = 5, c = 'blue')
    plt.show()
