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
        self.F = np.array((0,0))
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

    def force(self,pl1,pl2):
        d = math.sqrt((pl1.r[0]-pl2.r[0])**2 + (pl1.r[1]-pl2.r[1])**2)
        F = -self.G * pl1.m * pl2.m/(d**3) * np.subtract(pl1.r,pl2.r)
        return F

    def __interact(self):
        for p in self.planets:
            for p2 in self.planets:
                if p2 != p:
                    F = self.force(p,p2)
                    p.F = np.add(p.F,F)
                    p.a = p.F/p.m    
            p.v = np.add(p.v,p.a * self.dt)
            p.r = np.add(p.r,p.v * self.dt)
            p.x_list.append(p.r[0])
            p.y_list.append(p.r[1])

    def interact(self,t):
        while self.t <= t:
            self.__interact()
            self.t += self.dt