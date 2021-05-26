import numpy as np
import math

class Gravity:
    def __init__(self):
        self.x1_list = []
        self.y1_list = []
        self.x2_list = []
        self.y2_list = []

    def init(self,m1,m2,r1,v1,r2,v2,dt = 60*6*24):
        self.G =  6.67408 * 10**(-11)
        self.m1 = m1
        self.m2 = m2
        self.r1 = r1
        self.v1 = v1
        self.r2 = r2
        self.v2 = v2
        self.x1_list.append(r1[0])
        self.y1_list.append(r1[1])
        self.x2_list.append(r2[0])
        self.y2_list.append(r2[1])
        self.t = 0
        self.dt = dt

    def __interact(self):
        # za prvo tijelo
        d1 = math.sqrt((self.r1[0]-self.r2[0])**2 + (self.r1[1]-self.r2[1])**2)
        self.a1 = -self.G * self.m2/(d1**3) * np.subtract(self.r1,self.r2)
        self.v1 = np.add(self.v1,self.a1*self.dt)
        self.r1 = np.add(self.r1,self.v1*self.dt)
        
        #za drugo tijelo
        d2 = math.sqrt((self.r2[0]-self.r1[0])**2 + (self.r2[1]-self.r1[1])**2)
        self.a2 = -self.G * self.m1/(d2**3) * np.subtract(self.r2,self.r1)
        self.v2 = np.add(self.v2,self.a2*self.dt)
        self.r2 = np.add(self.r2,self.v2*self.dt)

    def interact(self,t):
        while self.t <= t:
            self.__interact()
            self.x1_list.append(self.r1[0])
            self.y1_list.append(self.r1[1])
            self.x2_list.append(self.r2[0])
            self.y2_list.append(self.r2[1])
            self.t += self.dt