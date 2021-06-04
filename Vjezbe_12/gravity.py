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

    def force(self,m1,m2,r1,r2):
        d = math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)
        F = -self.G * m1 * m2/(d**3) * np.subtract(r1,r2)
        return F

    def __interact(self):
        for p in self.planets:
            F = np.array((0,0))
            for p2 in self.planets:
                if p2 == p:
                    F = 0
                else:
                    F = np.add(F,self.force(p.m,p2.m,p.r,p2.r))
                    #p2.a = F/p2.m
                    #p2.v = np.add(p2.v,p2.a*self.dt)
                    #p2.r = np.add(p2.r,p2.v*self.dt)
            p.F = F
            p.a = p.F/p.m
            p.v = np.add(p.v,p.a * self.dt)
            p.r = np.add(p.r,p.v * self.dt)
            p.x_list.append(p.r[0])
            p.y_list.append(p.r[1])

    def interact(self,t):
        while self.t <= t:
            self.__interact()
            self.t += self.dt