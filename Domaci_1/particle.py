import matplotlib.pyplot as plt
import math

class Particle:
    def init(self,v0,theta,x0,y0,dt):
        self.v0 = v0
        self.theta = theta
        self.xi = x0
        self.yi = y0
        self.dt = dt
        self.x = []
        self.y = []
        self.v = []
        self.x.append(self.xi)
        self.y.append(self.yi)
        self.kut = self.theta*math.pi/180
        self.vx = self.v0*math.cos(self.kut)
        self.vy = self.v0*math.sin(self.kut)

    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.xi = 0
        self.yi = 0
        self.dt = 0
        self.x = []
        self.y = []
        self.v = []
        self.kut = 0
        self.v0x = 0
        self.v0y = 0

    def __move(self):
        a = 9.81
        self.xi = self.xi + self.vx*self.dt
        self.vy = self.vy - a*self.dt
        self.yi = self.yi + self.vy*self.dt
        self.x.append(self.xi)
        self.y.append(self.yi)
        self.vi = math.sqrt(self.vx**2 + self.vy**2)
        self.v.append(self.vi)

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

    def total_time(self):
        t = 0
        while self.yi >= 0:
            self.__move()
            t = t + self.dt
        return t
        
    def max_speed(self):
        while self.yi >= 0:
            self.__move()
        return max(self.v)

    def velocity_to_hit_target(self,mx,my,r):
        d_meta = math.sqrt(mx**2 + my**2)

    def angle_to_hit_target(self,mx,my,r):
        d_meta = math.sqrt(mx**2 + my**2)
