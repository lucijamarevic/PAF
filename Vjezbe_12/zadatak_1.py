import gravity as g
import numpy as np
import matplotlib.pyplot as plt

au = 1.486*(10**11)
dan = 60*60*24

ms =  1.989 * (10**30)
mz =  5.9742 * (10**24)
vs = np.array((0,0))
rs = np.array((0,0))
vz = np.array((0,29783))
rz = np.array((au,0))

S = g.Planet(ms,vs,rs) #(m,v,r)
Sun = S.return_list()
E = g.Planet(mz,vz,rz)
Earth = E.return_list()

p = g.Universe()
p.add_planet(Sun)
p.add_planet(Earth)

p.interact(365.242*dan)

plt.figure("Solar system", figsize=(7,7))
ax = plt.axes()
#ax.set_facecolor("black")
plt.plot(p.x_list[0],p.y_list[0], c = "yellow", label = "Sun")
plt.plot(p.x_list[1],p.y_list[1], c = "blue", label = "Earth")
plt.legend()
plt.show()