import matplotlib.pyplot as plt
import math

class Particle:
    def init(self,v0,theta,x0,y0):
        self.v0 = v0
        self.theta = theta
        self.xi = x0
        self.yi = y0
        self.x = []
        self.y = []
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
        self.x = []
        self.y = []
        self.kut = 0
        self.v0x = 0
        self.v0y = 0

    def __move(self,delta_t):
        a = 9.81
        dt = delta_t/1000
        for i in range(1000):
            self.xi = self.xi + self.vx*dt
            self.vy = self.vy - a*dt
            self.yi = self.yi + self.vy*dt
            if self.yi >= 0:
                self.x.append(self.xi)
                self.y.append(self.yi)

    def range(self):
        self.__move(20)
        return max(self.x)

    def plot_trajectory(self):
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x,self.y)
        plt.title("x-y graf")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()