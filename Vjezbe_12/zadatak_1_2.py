import gravity as g
import numpy as np
import matplotlib.pyplot as plt

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

ms =  1.989 * (10**30)  #Sun
mz =  5.9742 * (10**24)
vs = np.array((0,0))

rs = np.array((0,0))  #Earth
vz = np.array((0,29783))
rz = np.array((au,0))

Sun = g.Planet("Sun","yellow",ms,vs,rs) 
Earth = g.Planet("Earth","blue",mz,vz,rz)

p = g.Universe()
p.add_planet(Sun)
p.add_planet(Earth)
#print(p.planets) sprema ih u listu kao objekte iz klase Planet

p.interact(year)

plt.plot(Sun.x_list,Sun.y_list, c = Sun.color, label = Sun.name)
plt.plot(Earth.x_list,Earth.y_list, c = Earth.color, label = Earth.name)
plt.legend()
plt.show()