import harmonic_oscillator as ho 
import matplotlib.pyplot as plt

h1 = ho.HarmonicOscillator()

h1.init(0.1,2,0,0.5,0.01)
print("Period titranja iznosi: {:.2f}".format(h1.period()))
print("Analiticki period titranja iznosi: {:.2f}".format(h1.period_analitic()))

print("Pogreska je: ")