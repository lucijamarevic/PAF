import matplotlib.pyplot as plt
import math
import particle as prt

p1 = prt.Particle()

p1.init(10,60,0,0,0.01)
print("Ukupno vrijeme trajanja gibanje iznosi: {:.2f}s".format(p1.total_time()))
print("Najveca ostvarena brzina iznosi: {:.2f}m/s".format(p1.max_speed()))