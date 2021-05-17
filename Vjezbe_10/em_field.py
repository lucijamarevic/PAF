import numpy as np
import math

class em_field:
    #mi0 = 4*math.pi*(10**(-7))
    def __init__(self):
        self.lista = []

    def init(self,q,v0x,v0y,v0z,Ex,Ey,Ez,Bx,By,Bz):
        self.q = q
        self.vx = v0x
        self.vy = v0y
        self.vz = v0z
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez
        self.Bx = Bx
        self.By = By
        self.Bz = Bz