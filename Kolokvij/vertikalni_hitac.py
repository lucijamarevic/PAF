class VertikalniHitac:
    def init(self,h0,v0):
        self.h0 = h0
        self.hi = self.h0
        self.v0 = v0
        self.vi = self.v0
        self.ti = 0
        self.h = []
        self.v = []
        self.t = []
        self.h.append(self.hi)
        self.v.append(self.vi)
        self.t.append(self.ti)
        
        print("Objekt je uspjesno storen.")
        print("Pocetna visina iznosi: {:.2f}m, a pocetna brzina: {:.2f}m/s".format(h0,v0))

    def reset():
        del self.h0s
        del self.hi
        del self.v0
        del self.vi
        del self.ti
        del self.h 
        del self.v 
        del self.t

    def change_height(self,novi_h0):
        self.h0 = novi_h0
        self.hi = self.h0
        print("Nova pocetna visina iznosi: {:.2f}m".format(self.h0))

    def change_speed(self,novi_v0):
        self.v0 = novi_v0
        self.vi = self.v0
        print("Nova pocetna brzina iznosi: {:.2f}m/s".format(self.v0))

    def move(self,dt):
        g = 9.81
        while self.hi >= 0:
            self.vi = self.vi - g*dt
            self.hi = self.hi + self.vi*dt
            self.ti += dt
            self.h.append(self.hi)
            self.v.append(self.vi)
            self.t.append(self.ti)
        return self.h, self.v, self.t 

    def max_height(self,dt):
        self.move(dt)
        h_max = max(self.h)
        return h_max

    def total_time(self,dt):
        self.move(dt)
        t_uk = max(self.t)
        return t_uk
