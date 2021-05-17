import numpy as np
import math

class em_field:
    #mi0 = 4*math.pi*(10**(-7))
    def __init__(self):
        self.r_lista = []
        self.v_lista = []
        self.t_lista = []

    def init(self,m,q,x0,y0,z0,v0x,v0y,v0z,Ex,Ey,Ez,Bx,By,Bz,dt):
        self.m = m
        self.q = q
        self.x = x0
        self.y = y0
        self.z = z0
        self.r = np.array((x0,y0,z0))
        self.r_lista.append(self.r)
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
        self.dt = 0
        self.t = 0
        self.t_lista.append(self.t)