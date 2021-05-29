import numpy as np
import math

class Planet:
    def __init__(self,m,v,r):
        lista = [m,v,r]
        return lista

class Gravity:
    def __init__(self,dt = 60*6*24):
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.dt = dt
        self.planeti = []

    def add_planet(self,planet):
        self.planeti.append(planet)

    def __interact(self,m,v,r):
        a = []
        self.m = m
        self.v = v
        self.r = r

        for p2 in self.planeti:
            self.m2 = p2[0]
            self.v2 = p2[1]
            self.r2 = p2[2]

            d = math.sqrt((self.r[0]-self.r2[0])**2 + (self.r[1]-self.r2[1])**2)
            self.ai = -self.G * self.m2/(d**3) * np.subtract(self.r,self.r2)

            a.append(self.ai)

        self.a = 0
        for i in range(0,len(a),2):
                self.a = np.add(self.a,np.add(a[i],a[i+1]))

        self.v = np.add(self.v,self.a*self.dt)
        self.r = np.add(self.r,self.v*self.dt)

    def interact(self,t):
        for p in self.planeti:
            m = p[0]
            v = p[1]
            r = p[2]
            i = self.planeti.index(p)
            del self.planeti[p]

            while self.t <= t:
                self.__interact(m,v,r)
                self.t += self.dt