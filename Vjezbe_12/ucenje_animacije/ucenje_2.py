import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure() 
axis = plt.axes(xlim =(-50, 50),
                ylim =(-50, 50)) 
  
line, = axis.plot([], [], lw = 2) 
   
# what will our line dataset contain?
def init(): 
    line.set_data([], []) 
    return line, 
   
# initializing empty value for x and y co-ordinates
xdata, ydata = [], [] 

# animation function 
def animate(i): 
    t = 0.1 * i 
    x = t * np.sin(t) 
    y = t * np.cos(t) 
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
      
    return line,


# calling the animation function     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = 500, interval = 20, blit = True) 

plt.show()