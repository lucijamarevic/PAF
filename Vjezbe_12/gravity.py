import numpy as np
import math

class Planet: 
    def __init__(self,m,v,r): 
        self.list = [m,v,r]

    def return_list(self):
        return self.list

class Universe:
    def __init__(self,dt = 60*6*24):
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.dt = dt
        self.planeti = []
        self.x_list = []
        self.y_list = []

    def add_planet(self,planet): 
        self.planeti.append(planet)

    def __reset_1(self):
        self.m = 0
        self.r = np.array((0,0))
        self.v = np.array((0,0))
        self.a = np.array((0,0))
        self.F = np.array((0,0))
        self.x = []
        self.y = []
        self.t = 0

    def __reset_2(self):
        self.m2 = 0
        self.r2 = np.array((0,0))
        self.v2 = np.array((0,0))

    #ode dalje je negdi greska

    def force(self,m1,m2,r1,r2):
        d = math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)
        sila = -self.G * m1*m2/(d**3) * np.subtract(r1,r2)
        return sila

    def __interact(self,m,v,r):
        self.x = []
        self.y = []
        self.m = m
        self.v = v
        self.r = r
        self.F = np.array((0,0))

        for p2 in self.planeti:
            self.m2 = p2[0]
            self.v2 = p2[1]
            self.r2 = p2[2]

            if self.m2 == self.m:
                F = np.array((0,0))
            
            else:
                F = self.force(self.m,self.m2,self.r,self.r2)
                
            self.F = np.add(self.F,F)
            self.__reset_2()
        
        self.a = self.F/self.m
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
            self.__reset_1()