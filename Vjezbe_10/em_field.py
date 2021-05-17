import numpy as np
import math

class EmField:
    #mi0 = 4*math.pi*(10**(-7))
    def __init__(self):
        self.r_lista = []
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []
        self.v_lista = []
        self.a_lista = []
        self.t_lista = []

    def init(self,m,q,x0,y0,z0,v0x,v0y,v0z,Ex,Ey,Ez,Bx,By,Bz,dt):
        self.m = m
        self.q = q
        self.x = x0
        self.y = y0
        self.z = z0
        self.r = np.array((x0,y0,z0))
        self.r_lista.append(self.r)
        self.x_lista.append(x0)
        self.y_lista.append(y0)
        self.z_lista.append(z0)
        self.vx = v0x
        self.vy = v0y
        self.vz = v0z
        self.v = np.array((v0x,v0y,v0z))
        self.v_lista.append(self.v)
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez
        self.E = np.array((Ex,Ey,Ez))
        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.B = np.array((Bx,By,Bz))
        self.a = self.__akceleracija(self.v)
        self.a_lista.append(self.a)
        self.dt = 0
        self.t = 0
        self.t_lista.append(self.t)

        print(self.a)

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
            