import matplotlib.pyplot as plt
import numpy as np
import math 

class Projectile:
    g = -9.81
    def init(self,m,v0,theta,x0,y0,ro,cd,A,dt):
        self.m = m
        self.v0 = v0         # za brzine
        self.theta = theta
        self.kut = self.theta*math.pi/180
        self.vx = self.v0*math.cos(self.kut)
        self.vy = self.v0*math.sin(self.kut)
        self.vx_list = []
        self.vy_list = []
        self.vx_list.append(self.vx)
        self.vy_list.append(self.vy)
        self.x = x0          # za polozaj
        self.y = y0
        self.x_list = []
        self.y_list = []
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.ro = ro         # za akceleraciju
        self.cd = cd
        self.A = A
        self.ax = -sgn(self.vx)*(self.ro*self.cd*self.A/(2*m))*self.vx**2
        self.ay = -g-sgn(self.vy)*(self.ro*self.cd*self.A/(2*m))*self.vy**2
        self.ax_list = []
        self.ay_list = []
        self.ax_list.append(self.ax)
        self.ay_list.append(self.ay)
        self.dt = dt
 
    def reset(self):
        self.m = 0
        self.v0 = 0        
        self.theta = 0
        self.vx = 0
        self.vy = 0
        self.vx_list = []
        self.vy_list = []
        self.x = 0
        self.y = 0
        self.x_list = []
        self.y_list = []
        self.ro = 0
        self.cd = 0
        self.A = 0
        self.ax = 0
        self.ay = 0
        self.ax_list = []
        self.ay_list = []
        self.dt = 0

    def __move(self):
        self.vx += self.ax*self.dt      # x-smjer
        self.x += self.vx*self.dt
        self.ax = -sgn(self.vx)*(self.ro*self.cd*self.A/(2*m))*self.vx**2
        self.x_list.append(self.x)
        self.vx_list.append(self.v)
        self.ax_list.append(self.ax)
        self.vy += self.ay*self.dt      #y-smjer
        self.y += self.vy*self.dt
        self.ay = -g-sgn(self.vy)*(self.ro*self.cd*self.A/(2*m))*self.vy**2

    def range(self):
        while self.yi >= 0:
            self.__move()
        return max(self.x)

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*self.kut))/9.81
        return D

    def plot_trajectory(self):
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x,self.y)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()