import math
import matplotlib.pyplot as plt

class HarmonicOscilator:
    def init(self,m,k,v0,A,dt):
        self.m = m
        self.k = k
        self.ai = (-k/m) * A 
        self.vi = v0
        self.xi = A
        self.dt = dt
        self.ti = 0
        self.t = []
        self.a = []
        self.v = []
        self.x = []
        self.t.append(self.ti)
        self.a.append(self.ai)
        self.v.append(self.vi)
        self.x.append(self.xi)

    def oscilate(self,t):
        n = t/self.dt
        for i in range(round(n)):
            self.vi = self.vi + self.ai * self.dt
            self.xi = self.xi + self.vi * self.dt
            self.ai = (-self.k/self.m) * self.xi
            self.ti += self.dt
            self.v.append(self.vi)
            self.x.append(self.xi)
            self.a.append(self.ai)
            self.t.append(self.ti)

    def plot_trajectory(self):
        plt.figure("Harmonic oscilator")
        fig = plt.subplot()
        plt.subplot(2,2,1)
        plt.plot(self.t,self.x)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("x-t graf")
        plt.subplot(2,2,2)
        plt.plot(self.t,self.v)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.title("v-t graf")
        plt.subplot(2,2,3)
        plt.plot(self.t,self.a)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        plt.title("a-t graf")
        plt.subplots_adjust(wspace = 0.4, hspace = 0.6)
        plt.show()
