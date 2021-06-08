import gravity as g
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = g.Planet("Sun","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Earth = g.Planet("Earth","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))

p = g.Universe() 
p.add_planet(Sun)
p.add_planet(Earth)

p.interact(5*year)

def data_gen():
    gen_list = ([Earth.x_list[i],Earth.y_list[i]] for i in range(len(Earth.x_list)))
    return gen_list

def init():
    return point

fig, ax = plt.subplots()
point, = ax.plot([0], [0], 'go')
point.set_data(0, 0)
 
def run(data):
 
    x, y = data
         
    point.set_data(x, y)
     
    return point
 
ani = animation.FuncAnimation(fig, run, data_gen, init_func=init,interval=10)

plt.show()