import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

class EmField:
    def __init__(self):
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []

    def init(self,m,q,r,v,E,B,dt):    #sve dobro
        self.m = m
        self.q = q
        self.r = r
        self.x_lista.append(self.r[0])
        self.y_lista.append(self.r[1])
        self.z_lista.append(self.r[2])
        self.v = v
        self.E = E
        self.B = B
        self.a = self.__akceleracija(self.v)
        self.dt = dt
        self.t = 0

    def reset(self):
        self.m = 0
        self.q = 0
        self.r = 0
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []
        self.v = 0
        self.E = 0
        self.B = 0
        self.a = 0
        self.dt = 0
        self.t = 0

    def __akceleracija(self,v):
        return (self.q/self.m) * (np.add(self.E,np.cross(v,self.B)))

    def __move(self):
        self.v = np.add(self.v,self.a*self.dt)
        self.r = np.add(self.r,self.v*self.dt)
        self.a = self.__akceleracija(self.v)
        self.t += self.dt
    
    def move(self,t):
        while self.t <= t:
            self.__move()
            self.x_lista.append(self.r[0])
            self.y_lista.append(self.r[1])
            self.z_lista.append(self.r[2])

    def plot_trajectory(self):
        ax = plt.axes(projection = "3d")
        ax.plot3D(self.x_lista,self.y_lista,self.z_lista)
        plt.show()            