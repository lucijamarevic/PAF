import gravity as g
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = g.Planet("Sun","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Pluto = g.Planet("Pluto", "gray", 1.309 * (10**22), np.array((0,46700)), np.array((29*au,0)))
##Earth = g.Planet("Earth","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))

p = g.Universe() 
p.add_planet(Sun)
p.add_planet(Pluto)
##p.add_planet(Earth)

p.interact(250*year) 

plt.style.use('dark_background')
fig = plt.figure("Solar system", figsize = (8,8)) 
axis = plt.axes(xlim = (-40*au,40*au),
                ylim = (-40*au,40*au)) 

axis.plot(Sun.x_list,Sun.y_list, c = Sun.color, label = Sun.name, linewidth = 2)
axis.plot(Pluto.x_list,Pluto.y_list, c = Pluto.color, label = Pluto.name, linewidth = 2)
##axis.plot(Earth.x_list,Earth.y_list, c = Earth.color, label = Earth.name)

lines = []
#planets = [Sun, Mercury, Venus, Earth, Mars]
planets = [Sun, Pluto]

for obj in planets:
    line = axis.plot([],[], "o", c = obj.color)[0]
    lines.append(line)
   
def init():
    for line in lines: 
        line.set_data([], []) 
    return lines

def animate(i):
    for index, obj in enumerate(planets):
        x = obj.x_list[i] 
        y = obj.y_list[i]
        lines[index].set_data(x,y) 
      
    return lines
     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = len(Sun.x_list), interval = 10, blit = True) 

plt.axis('off') 
plt.legend(loc = "upper right")
plt.show()