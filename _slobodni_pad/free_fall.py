import matplotlib.pyplot as plt
import math 

class Particle:
    def __init__(self):
        self.v_list = []
        self.h_list = []
        self.t_list = []

    def init(self,m,v0,h0,dt = 0.01):  ##ako korisnik ne unese dt, on ce po defaultu biti 0.01
        self.m = m
        self.v0 = v0         
        self.v = v0
        self.h0 = h0
        self.h = h0
        self.dt = dt
        self.t = 0
        self.h_list.append(self.h)
        self.v_list.append(self.v)
        self.t_list.append(self.t)
 
    def reset(self):
        self.m = 0
        self.v0 = 0        
        self.v = 0
        self.h0 = 0
        self.h = 0
        self.h_list.clear()
        self.v_list.clear()
        self.t_list.clear()
        self.dt = 0

    def __move(self):
        a = 9.81
        self.v -= a*self.dt    ## - ide jer je g usmjerena prema dolje
        self.h += self.v*self.dt
        self.h_list.append(self.h)
        self.v_list.append(self.v)

    def move(self):
        while self.h >= 0:
            self.__move()
            self.t += self.dt
            self.t_list.append(self.t)

        return self.h_list, self.v_list, self.t_list


    ### alternativno mozemo napraviti i ovako, ista je stvar

    def move_2(self):
        a = 9.81
        while self.h >= 0:
            self.v -= a*self.dt    ## - ide jer je g usmjerena prema dolje
            self.h += self.v*self.dt
            self.h_list.append(self.h)
            self.v_list.append(self.v)
            self.t += self.dt
            self.t_list.append(self.t)

        return self.h_list, self.v_list, self.t_list