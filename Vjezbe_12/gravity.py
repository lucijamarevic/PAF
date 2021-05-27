import numpy as np
import math

class Planet:
    def __init__(self,m,r,v):
        lista = [m,r,v]   #spreman vrijednosti za planet
        return lista

class Gravity:
    def __init__(self,dt = 60*6*24):
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.dt = dt
        self.planeti = []

    def add_planet(self,planet):
        self.planeti.append(planet)   #spreman planete u listu

    #ovo dalje napola valja ahahah
    def __interact(self):
        for p in self.list:
            self.m = p[0]
            self.v = p[1]
            self.r = p[2]
        
            ds = math.sqrt((self.rs[0]-self.r[0])**2 + (self.rs[1]-self.r[1])**2)
            self.as = -self.G * self.m/(ds**3) * np.subtract(self.rs,self.r)
            self.vs = np.add(self.vs,self.as*self.dt)
            self.rs = np.add(self.rs,self.vs*self.dt)
            
            d = math.sqrt((self.r[0]-self.rs[0])**2 + (self.r[1]-self.rs[1])**2)
            self.a = -self.G * self.ms/(d**3) * np.subtract(self.r,self.rs)
            self.v = np.add(self.v,self.a*self.dt)
            self.r = np.add(self.r,self.v*self.dt)

    def interact(self,t):
        while self.t <= t:
            self.__interact()
            #self.x1_list.append(self.r1[0])
            #self.y1_list.append(self.r1[1])
            #self.x2_list.append(self.r2[0])
            #self.y2_list.append(self.r2[1])
            self.t += self.dt

        #return self.x1_list, self.y1_list, self.x2_list , self.y2_list