import matplotlib.pyplot as plt
import math

class HarmonicOscillator:
    def init(self,m,k,v0,A,dt):
        self.m = m
        self.k = k
        self.ai = (-k/m) * A 
        self.vi = v0
        self.x0 = A
        self.xi = self.x0
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

    def reset(self):
        del self.m
        del self.k
        del self.ai
        del self.vi
        del self.xi
        del self.dt
        del self.ti
        del self.t
        del self.a
        del self.v
        del self.x

    def oscillate(self, t):
        while self.ti <= t:
            self.vi = self.vi + self.ai * self.dt
            self.xi = self.xi + self.vi * self.dt
            self.ai = (-self.k/self.m) * self.xi
            self.ti += self.dt
            self.v.append(self.vi)
            self.x.append(self.xi)
            self.a.append(self.ai)
            self.t.append(self.ti)
  
        return self.x, self.t

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

    def analitic_x(self,t):
        self.x = []
        self.t = []
        self.omega = math.sqrt(self.k/self.m)
        self.fi = math.pi/2
        self.ti = 0
        while self.ti <= t:
            xi = self.xi * math.sin(self.omega*self.ti + self.fi)
            self.ti += self.dt
            self.x.append(xi)
            self.t.append(self.ti)
            
        return self.x, self.t

    ## ovo ne valja, ali ne znan zasto
    def period(self):
        t = 0
        vi = self.vi
        xi = self.x0
        ai = self.ai
        x = []
        while True:
            vi = vi + ai * self.dt
            xi = xi + vi * self.dt
            ai = (-self.k/self.m) * xi
            t += self.dt
            x.append(xi)
            if xi >= self.x0 - self.dt/100 or xi <= self.x0 + self.dt/100:
                break
        #print(x)
        T = 2*t
        return T
    
    ## ovo ne valja jer mi u ovoj verziji metoda oscillate racuna sve dok self.ti
    ## ne dode do zadanog vremena (uvjet while self.ti <= t) pa ce u svakom pokusaju 
    ## period ispasti 2*zadano vrijeme
    def period(self):
        while True:
            self.oscillate(1)
            if self.xi >= self.x0 - self.dt or self.xi <= self.x0 + self.dt:
                break
        print(self.x)
        T = 2*self.ti
        return T

    def period_analitic(self):
        return 2*math.pi*math.sqrt(self.m/self.k)