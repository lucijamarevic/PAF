import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math

class Planet: 
    def __init__(self,name,color,m,v,r): 
        self.name = name
        self.color = color
        self.m = m
        self.v0 = v
        self.v = v
        self.r0 = r
        self.r = r
        self.x_list = []
        self.y_list = []
        self.x_list.append(self.r[0])
        self.y_list.append(self.r[1])

    def reset(self):
        self.v = self.v0
        self.r = self.r0
    
class Universe:
    def __init__(self):
        self.dt = 60*6*24
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.planets = []

    def add_planet(self,planet):
        self.planets.append(planet)

    def __acc(self,pl1,pl2):
        d = math.sqrt((pl1.r[0]-pl2.r[0])**2 + (pl1.r[1]-pl2.r[1])**2)
        a = -self.G * pl2.m/(d**3) * np.subtract(pl1.r,pl2.r)
        return a

    def __interact(self):
        for p in self.planets:
            p.a = np.array((0,0))
            for p2 in self.planets:
                if p2 != p:
                    a = self.__acc(p,p2)
                    p.a = np.add(p.a,a)    
            p.v = np.add(p.v,p.a * self.dt)
            p.r = np.add(p.r,p.v * self.dt)
            p.x_list.append(p.r[0])
            p.y_list.append(p.r[1])

    def interact(self,t):
        while self.t <= t:
            self.__interact()
            self.t += self.dt 

# ovo dalje ne valja
class Animation:
    def __init__(self,x_list,y_list,objects):
        self.fig = plt.figure() 
        axis = plt.axes() 
  
        self.line, = axis.plot([], []) 

        self.x_list = x_list
        self.y_list = y_list
        self.objects = objects

        self.xdata = []
        self.ydata = []

    def init(self): 
        self.line.set_data([], []) 
        return self.line,

    def animate(self,i): 
        t = 0.1 * i 
        #self.xdata.append(x) 
        #self.ydata.append(y) 
        self.line.set_data(self.xdata, self.ydata) 
        
        return self.line,