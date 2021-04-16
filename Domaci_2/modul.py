import matplotlib.pyplot as plt 

class Particle:
    def init(self,f,x0,v0,total_time,dt):
        self.f = f
        self.x0 = x0
        self.v0 = v0
        self.t_uk = total_time
        self.dt = dt

    def reset(self):
        del self.f
        del self.x0
        del self.v0
        del self.t_uk
        del self.dt