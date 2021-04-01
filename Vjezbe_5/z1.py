import harmonic_oscilator as ho 

h1 = ho.HarmonicOscilator()

h1.init(0.1,2,0,0.5,0.1)
h1.oscilate(10)
h1.plot_trajectory()