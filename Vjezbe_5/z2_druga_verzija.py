import harmonic_oscillator as ho 
import matplotlib.pyplot as plt
import numpy as np

h1 = ho.HarmonicOscillator()

dt_lista = list(np.linspace(0.01,0.1, 20))
aps_pogreska = []

for dt in dt_lista:
    h1.init(0.1,5,0,0.5,dt)    #(m,k,v0,A,dt)
    greska = (abs(h1.period() - h1.period_analitic()) / h1.period_analitic()) * 100
    aps_pogreska.append(greska)

plt.plot(dt_lista, aps_pogreska)
plt.xlabel("dt [s]")
plt.ylabel("absolute error [%]")
plt.title("preciznost numerickog racunanja perioda")
plt.show()