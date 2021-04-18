import matplotlib.pyplot as plt

class Particle:
    def init(self,func,m,x0,v0,total_time,dt):
        self.func = func
        self.m = m
        self.xi = x0
        self.vi = v0
        self.ti = 0
        self.fi = self.func(self.vi, self.xi, self.ti)
        self.ai = self.fi/self.m
        self.t_uk = total_time
        self.dt = dt
        self.t = []
        self.f = []
        self.a = []
        self.v = []
        self.x = []
        self.t.append(self.ti)
        self.f.append(self.fi)
        self.a.append(self.ai)
        self.v.append(self.vi)
        self.x.append(self.xi)
    
    def reset(self):
        del self.F
        del self.m
        del self.ai
        del self.xi
        del self.vi
        del self.ti
        del self.t_uk
        del self.dt
        del self.t
        del self.a
        del self.v
        del self.x

    def move(self):
        while self.ti <= self.t_uk:            
            self.ti += self.dt
            self.vi = self.vi + self.ai * self.dt
            self.xi = self.xi + self.vi * self.dt
            self.fi = self.func(self.vi,self.xi,self.ti)
            self.ai = self.fi/self.m
            self.t.append(self.ti)
            self.v.append(self.vi)
            self.x.append(self.xi)
            self.f.append(self.fi)
            self.a.append(self.ai)

        return self.x, self.v, self.a, self.t

    def plot_trajectory(self):
        self.move()
        plt.figure("Movement description")
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
        plt.subplot(2,2,4)
        plt.plot(self.t,self.f)
        plt.xlabel("t [s]")
        plt.ylabel("F [N]")
        plt.title("F-t graf")
        plt.subplots_adjust(wspace = 0.4, hspace = 0.6)
        plt.show()