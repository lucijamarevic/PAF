import harmonic_oscillator as ho 
import matplotlib.pyplot as plt

h1 = ho.HarmonicOscillator()

h1.init(0.1,2,0,0.5,0.01)
h1.oscillate(5)
h1.plot_trajectory()