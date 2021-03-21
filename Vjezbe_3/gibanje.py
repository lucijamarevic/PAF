import matplotlib.pyplot as plt
import math
import particle as prt

p1 = prt.Particle()

p1.init(100,45,0,0)
print(f"Dome je {p1.range()}m.")
p1.plot_trajectory()
p1.reset()

p1.init(10,60,0,0)
print(f"Domet je {p1.range()}m.")
p1.plot_trajectory()
p1.reset()