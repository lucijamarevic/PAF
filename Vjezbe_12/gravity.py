import numpy as np
import math

class Planet: 
    def __init__(self,m,v,r):     #radi 
        self.list = [m,v,r]

    def return_list(self):     #radi
        return self.list

class Universe:
    def __init__(self,dt = 60*6*24):     #radi
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.dt = dt
        self.planeti = []
        self.x_list = []
        self.y_list = []

    def add_planet(self,planet):     #radi
        self.planeti.append(planet)


    #ode dalje je negdi greska

    def __interact(self,m,v,r):
        self.x = []
        self.y = []
        self.m = m
        self.v = v
        self.r = r
        self.a = 0

        for p2 in self.planeti:
            self.m2 = p2[0]
            self.v2 = p2[1]
            self.r2 = p2[2]

            if self.m2 == self.m:
                pass
            
            else:
                d = math.sqrt((self.r[0]-self.r2[0])**2 + (self.r[1]-self.r2[1])**2)
                a = -self.G * self.m2/(d**3) * np.subtract(self.r,self.r2)
                self.a = np.add(self.a,a)

        self.v = np.add(self.v,self.a*self.dt)
        self.r = np.add(self.r,self.v*self.dt)

        self.x.append(self.r[0])
        self.y.append(self.r[1])

    def interact(self,t):
        for p in self.planeti:
            m = p[0]
            v = p[1]
            r = p[2]

            while self.t <= t:
                self.__interact(m,v,r)
                self.t += self.dt

            self.x_list.append(self.x)
            self.y_list.append(self.y)
            self.x.clear()
            self.y.clear()