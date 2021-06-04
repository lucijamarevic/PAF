import gravity as g
import numpy as np
import matplotlib.pyplot as plt

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = g.Planet("Sun","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Mercury = g.Planet("Mercury","orange",3.3 * (10**24),np.array((-47362,0)),np.array((0,0.466*au)))
Venus = g.Planet("Venus","red",4.8685 * (10**24),np.array((0,35020)),np.array((0.723*au,0)))
Earth = g.Planet("Earth","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))
Mars = g.Planet("Mars","brown",6.417 * (10**23),np.array((24007,0)),np.array((0,-1.667*au)))

p = g.Universe()
p.add_planet(Sun)
p.add_planet(Mercury)
p.add_planet(Venus)
p.add_planet(Earth)
p.add_planet(Mars)
#print(p.planets) sprema ih u listu kao objekte iz klase Planet

p.interact(year)

plt.plot(Sun.x_list,Sun.y_list, c = Sun.color, label = Sun.name) #linewidth = 5
plt.plot(Mercury.x_list,Mercury.y_list, c = Mercury.color, label = Mercury.name)
plt.plot(Venus.x_list,Venus.y_list, c = Venus.color, label = Venus.name)
plt.plot(Earth.x_list,Earth.y_list, c = Earth.color, label = Earth.name)
plt.plot(Mars.x_list,Mars.y_list, c = Mars.color, label = Mars.name)
plt.legend()
plt.show()