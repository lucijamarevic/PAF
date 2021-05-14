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

    def init(self,m,v0,theta,x0,y0,ro,cd,tijelo,a,dt):
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
        self.x0 = x0
        self.y0 = y0
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.ro = ro         # za akceleraciju
        self.cd = cd
        self.tijelo = tijelo
        self.a = a
        if tijelo == "kocka":
            self.A = a**2
        elif tijelo == "kugla":
            self.A = (a**2)*math.pi
        self.ax = 0
        self.ay = 0
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
    
    def __ax(self,v):
        return -abs(self.vx*self.vx*self.ro*self.cd*self.A)/(2*self.m)

    def __ay(self,v):
        return -9.81-abs(self.vy*self.vy*self.ro*self.cd*self.A)/(2*self.m)
    
    def __runge_kutta(self):
        # za x kommponentu 
        k1vx = self.__ax(self.vx)*self.dt 
        k1x = self.vx*self.dt
        k2vx = self.__ax(self.vx + k1vx/2)*self.dt
        k2x = (self.vx + k1vx/2)*self.dt        
        k3vx = self.__ax(self.vx + k2vx/2)*self.dt
        k3x = (self.vx + k2vx/2)*self.dt
        k4vx = self.__ax(self.vx + k3vx)*self.dt
        k4x = (self.vx + k3vx)*self.dt

        self.vx += (1/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
        self.x += (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
        
        self.ax = self.__ax(self.vx)

        # za y komponentu
        k1vy = self.__ay(self.vy)*self.dt 
        k1y = self.vy*self.dt
        k2vy = self.__ay(self.vy + k1vy/2)*self.dt
        k2y = (self.vy + k1vy/2)*self.dt
        k3vy = self.__ay(self.vy + k2vy/2)*self.dt
        k3y = (self.vy + k2vy/2)*self.dt
        k4vy = self.__ay(self.vy + k3vy)*self.dt
        k4y = (self.vy + k3vy)*self.dt

        self.vy += (1/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)
        self.y += (1/6)*(k1y + 2*k2y + 2*k3y + k4y)

        self.ay = self.__ay(self.vy)
    
    def runge_kutta(self):   
        while self.y >= 0:
            self.__runge_kutta()
            self.x_list.append(self.x)
            self.vx_list.append(self.vx)
            self.ax_list.append(self.ax)
            self.y_list.append(self.y)
            self.vy_list.append(self.vy)
            self.ay_list.append(self.ay)
            self.t += self.dt
            self.t_list.append(self.t)
        return self.x_list,self.y_list

    def angle_to_hit_target(self,mx,my,r):
        self.mx = mx
        self.my = my
        self.r = r
        d_lista = []
        th_lista = []
        min_lista = []

        # dio koji racuna kut
        pogodena = False
        for theta in range(91):
            d_lista = []
            th_lista = []
            self.init(self.m,self.v0,theta,self.x0,self.y0,self.ro,self.cd,self.tijelo,self.a,self.dt)
            while self.y > 0:   #vrsimo cijeli hitac
                self.__runge_kutta()
                D =  math.sqrt((self.mx-self.x)**2 + (self.my-self.y)**2)  #racunamo za svaki polozaj

                if D <= self.r:   #provjeravamo
                    pogodena = True   
                    kut = theta
                    break   #ako je meta pogodena prekidamo while petlju
                else:
                    d_lista.append(D - self.r)   #ako nije spremamo sve udaljenosti od mete za dani kut u listu

            if pogodena:
                break   #ako je meta pogodena prekidamo i for petlju
            else:
                d_min = min(d_lista)   #ako  nije, najmanja udaljenost za dani kut je minimum svih udaljenosti
                min_lista.append(d_min)   #spremamo minimume od svih kuteva 
                th_lista.append(theta)   #spremamo sve kuteve

        if pogodena:
            print("Potreban kut za pogoditi metu je: {}°".format(self.theta))
            
            # dio koji crta metu
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.init(self.m,self.v0,kut,self.x0,self.y0,self.ro,self.cd,self.tijelo,self.a,self.dt)
            self.runge_kutta()
            self.plot_trajectory()
            self.reset()
        
        else:
            d = min(min_lista)
            print("Nije moguce pogoditi metu sa zadanom brzinom.")
            print("Najmanja udaljenost od mete za zadanu brzinu je: {:.2f}m.".format(d))
            
            indeks = min_lista.index(d)
            th = th_lista[indeks]

            print("Kut za koji je projektil najblizi meti iznosi: {}°.".format(th))

            # dio koji crta metu
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.mx + self.r*math.cos(rad)
                x.append(xi)
                yi = self.my + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            # dio koji crta putanju
            self.init(self.m,self.v0,theta,self.x0,self.y0,self.ro,self.cd,self.tijelo,self.a,self.dt)
            self.runge_kutta()
            self.plot_trajectory()
            self.reset()