from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

class EmField:
    def __init__(self):
        self.r_lista = []
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []
        self.v_lista = []
        self.a_lista = []
        self.t_lista = []

    def init(self,m,q,r,v,E,B,dt):
        self.m = m
        self.q = q
        self.r = r
        self.r_lista.append(self.r)
        self.x_lista.append(self.r[0])
        self.y_lista.append(self.r[1])
        self.z_lista.append(self.r[2])
        self.v = v
        self.v_lista.append(self.v)
        self.E = E
        self.B = B
        self.a = self.__akceleracija(self.v)
        self.a_lista.append(self.a)
        self.dt = dt
        self.t = 0
        self.t_lista.append(self.t)

        print("akceleracija: {}".format(self.a))
        print("brzina: {}".format(self.v))
        print("polozaj: {}".format(self.r))
        print("x: {}, y: {}, z: {}".format(self.x_lista,self.y_lista,self.z_lista))

    def __akceleracija(self,v):
        return (self.q/self.m) * (np.add(self.E,np.cross(v,self.B)))

    def __move(self):
        self.v += self.a*self.dt
        self.r += self.v*self.dt
        self.a = self.__akceleracija(self.v)
        self.t += self.dt
    
    def move(self,t):
        while self.t <= t:
            self.__move
            self.r_lista.append(self.r)
            self.x_lista.append(self.r[0])
            self.y_lista.append(self.r[1])
            self.z_lista.append(self.r[2])
            self.v_lista.append(self.v)
            self.a_lista.append(self.a)
            self.t_lista.append(self.t)

    def plot_trajectory(self):
        ax = plt.axes(projection = "3d")
        ax.plot3D(self.x_lista,self.y_lista,self.z_lista, 'green')
        plt.show()
            