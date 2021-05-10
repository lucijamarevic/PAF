class BungeeJumping:
    g = 9.81
    def __init__(self):
        self.x_list = []
        self.t_list = []
        self.K_list = []
        self.U_list = []
        self.Eel_list = []
    
    def init(self,m,k,v0,h,l,ro,cd,A,dt):
        self.m = m
        self.k = k
        self.v = v0
        self.h = h
        self.x = h
        self.t = 0
        self.l = l
        self.a = -self.g
        self.ro = ro
        self.cd = cd
        self.A = A
        self.dt = dt
        self.K = 0
        self.U = m*self.g*h
        self.Eel = 0
        self.x_list.append(self.x)
        self.t_list.append(self.t)
        self.K_list.append(self.K)
        self.U_list.append(self.U)
        self.Eel_list.append(self.Eel)

    def reset(self):
        self.m = 0
        self.k = 0
        self.v = 0        
        self.x = 0
        self.t = 0
        self.ro = 0
        self.cd = 0
        self.A = 0
        self.dt = 0
        self.K = 0
        self.U = 0
        self.Eel = 0
        self.x_list = []
        self.t_list = []
        self.K_list = []
        self.U_list = []
        self.Eel_list = []

    def __dx(self,x):
        return abs(self.h - self.l - self.x)

    def __akcelracija(self,x):
        return (-self.k/self.m)*x + self.g

    def __akcelracija_ar(self,x,v):
        if v > 0:
            a = (-self.k/self.m)*x + self.g - (self.v*self.v*self.ro*self.cd*self.A)/(2*self.m)
        else:
            a = (-self.k/self.m)*x + self.g + (self.v*self.v*self.ro*self.cd*self.A)/(2*self.m)
        return a

    def __jump(self, oz):      
        self.v += self.a*self.dt
        self.x += self.v*self.dt
        dx = self.__dx(self.x)
        if oz == False:
            if self.x < self.h - self.l:
                self.a = -self.g
            else:
                self.a = self.__akcelracija(dx)
        else:
            self.a = self.__akcelracija_ar(dx,self.v)
        self.t += self.dt
        self.x_list.append(self.x)
        self.t_list.append(self.t)

    def jump(self, t, oz = True):
        while self.t <= t:
            self.__jump(oz)
  
        #return self.x, self.t

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