import matplotlib.pyplot as plt
import math
import particle as prt

p1 = prt.Particle()

p1.init(100,45,0,0,0.01)
print("Domet je {:.2f}m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()

p1.init(10,60,0,0,0.01)
print("Domet je {:.2f}m.".format(p1.range()))
p1.plot_trajectory()
p1.reset()  
