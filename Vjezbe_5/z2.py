import harmonic_oscillator as ho 
import matplotlib.pyplot as plt
import numpy as np

h1 = ho.HarmonicOscillator()

dt_lista = list(np.linspace(0.01,0.1, 20))
num_period = []
a_period = []

for dt in dt_lista:
    h1.init(0.1,5,0,0.5,dt)    #(m,k,v0,A,dt)
    num_period.append(h1.period())
    a_period.append(h1.period_analitic())

plt.plot(dt_lista, a_period, label = "analiticki period")
plt.scatter(dt_lista, num_period, s = 3, c = "orange", label = "numericki period")
plt.xlabel("dt [s]")
plt.ylabel("T [s]")
plt.title("preciznost numerickog racunanja perioda")
plt.legend(loc = "lower right")
plt.show()