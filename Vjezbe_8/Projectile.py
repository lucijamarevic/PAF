import matplotlib.pyplot as plt
import numpy as np
import math 

class Projectile:
    def __init__(self):
        self.vx_list = []
        self.vy_list = []
        self.x_list = []
        self.y_list = []
        self.ax_list = []
        self.ay_list = []
        self.t_list = []

    def init(self,m,v0,theta,x0,y0,ro,cd,A,dt):
        g = -9.81
        self.m = m
        self.v0 = v0         # za brzine
        self.theta = theta
        self.kut = self.theta*math.pi/180
        self.vx = self.v0*math.cos(self.kut)
        self.vy = self.v0*math.sin(self.kut)
        self.vx_list.append(self.vx)
        self.vy_list.append(self.vy)
        self.x = x0          # za polozaj
        self.y = y0
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.ro = ro         # za akceleraciju
        self.cd = cd
        self.A = A
        self.ax = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*self.vx**2
        self.ay = -g-np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*self.vy**2
        self.ax_list.append(self.ax)
        self.ay_list.append(self.ay)
        self.dt = dt
        self.t = 0
        self.t_list.append(self.t)
 
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
        g = -9.81
        self.vx += self.ax*self.dt      # x-smjer
        self.x += self.vx*self.dt
        self.ax = -np.sign(self.vx)*(self.ro*self.cd*self.A/(2*self.m))*self.vx**2
        self.x_list.append(self.x)
        self.vx_list.append(self.vx)
        self.ax_list.append(self.ax)
        self.vy += self.ay*self.dt      #y-smjer
        self.y += self.vy*self.dt
        self.ay = -g-np.sign(self.vy)*(self.ro*self.cd*self.A/(2*self.m))*self.vy**2
        self.y_list.append(self.y)
        self.vy_list.append(self.vy)
        self.ay_list.append(self.ay)

    def move(self):
        while self.y >= 0:
            self.__move()
            self.t += self.dt
            self.t_list.append(self.t)

    def range(self):
        self.move()
        return max(self.x)

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*self.kut))/9.81
        return D

    def total_time(self):
        self.move()
        return t

    def max_speed(self):
        self.move()
        return max(self.v)

    def plot_trajectory(self):
        self.move()
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x,self.y)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()