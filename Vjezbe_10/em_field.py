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

    def __euler(self):
        self.v = np.add(self.v,self.a*self.dt)
        self.r = np.add(self.r,self.v*self.dt)
        self.a = self.__akceleracija(self.v)
        self.t += self.dt
    
    def euler(self,t):
        while self.t <= t:
            self.__euler()
            self.x_lista.append(self.r[0])
            self.y_lista.append(self.r[1])
            self.z_lista.append(self.r[2])

        return self.x_lista, self.y_lista, self.z_lista

    def __runge_kutta(self):
        k1v = self.__akceleracija(self.v)*self.dt 
        k1r = self.v*self.dt
        k2v = self.__akceleracija(np.add(self.v,k1v/2))*self.dt
        k2r = (np.add(self.v,k1v/2))*self.dt
        k3v = self.__akceleracija(np.add(self.v,k2v/2))*self.dt
        k3r = (np.add(self.v,k2v/2))*self.dt
        k4v = self.__akceleracija(np.add(self.v,k3v))*self.dt
        k4r = (np.add(self.v,k3v))*self.dt

        self.v = np.add(self.v,(1/6)*np.add(np.add(k1v,2*k2v),np.add(2*k3v,k4v)))
        self.r = np.add(self.r,(1/6)*np.add(np.add(k1r,2*k2r),np.add(2*k3r,k4r)))
        self.a = self.__akceleracija(self.v)
        self.t += self.dt

    def runge_kutta(self,t):
        while self.t <= t:
            self.__runge_kutta()
            self.x_lista.append(self.r[0])
            self.y_lista.append(self.r[1])
            self.z_lista.append(self.r[2])

        return self.x_lista, self.y_lista, self.z_lista

    def plot_trajectory(self):
        ax = plt.axes(projection = "3d")
        ax.plot3D(self.x_lista,self.y_lista,self.z_lista)
        plt.show()            