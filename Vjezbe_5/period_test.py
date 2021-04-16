import harmonic_oscillator as ho 

h1 = ho.HarmonicOscillator()

h1.init(0.1,5,0,0.5,0.001)    #(m,k,v0,A,dt)
print("Period titranja iznosi: {:.2f}".format(h1.period()))
print("Analiticki period titranja iznosi: {:.2f}".format(h1.period_analitic()))

#h1.period()