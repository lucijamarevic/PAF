import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def init(self,v0,theta,x0,y0,dt):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.xi = self.x0
        self.y0 = y0
        self.yi = self.y0
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
        self.x0 = 0
        self.xi = 0
        self.y0 = 0
        self.yi = 0
        self.dt = 0
        self.x = []
        self.y = []
        self.v = []
        self.kut = 0
        self.vx = 0
        self.vy = 0

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
        while self.yi >= 0:
            self.__move()
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
        self.mx = mx
        self.my = my
        self.r = r
        d_list = []
        v_list = []

        # dio koji racunau brzinu
        pogodena = False
        for self.v0 in range(101):
            self.vx = self.v0*math.cos(self.kut)
            self.vy = self.v0*math.sin(self.kut)
            self.__move()
            D =  math.sqrt((self.mx-self.xi)**2 + (self.my-self.yi)**2) 
            if D <= self.r:
                pogodena = True
                break
            else: 
                d_list.append(D - self.r)
                v_list.append(self.v0)
        
        if pogodena:
            print("Potrebna brzina za pogoditi metu je: {:.2f}m/s".format(self.v0))

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
            self.init(self.v0,self.theta,self.x0,self.y0,self.dt )
            self.plot_trajectory()
            self.reset()

        else:
            d = min(d_list)
            print("Nije moguce pogoditi metu sa zadanim kutem.")
            print("Najmanja udaljenost od mete za zadani kut iznosti: {:.2f}".format(d))

            indeks = d_list.index(d)
            v = v_list[indeks]

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
            self.init(v,self.theta,self.x0,self.y0,self.dt )
            self.plot_trajectory()
            self.reset()
    
    def angle_to_hit_target(self,mx,my,r):
        self.mx = mx
        self.my = my
        self.r = r
        d_lista = []
        th_lista = []

        # dio koji racuna kut
        pogodena = False
        for self.theta in range(91):
            self.kut = self.theta*math.pi/180
            self.vx = self.v0*math.cos(self.kut)
            self.vy = self.v0*math.sin(self.kut)
            self.__move()
            D =  math.sqrt((self.mx-self.xi)**2 + (self.my-self.yi)**2) 
            if D <= self.r:
                pogodena = True
                break
            else:
                d_lista.append(D - self.r)
                th_lista.append(self.theta)

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
            self.init(self.v0,self.theta,self.x0,self.y0,self.dt )
            self.plot_trajectory()
            self.reset()
        
        else:      # ode nesto ne valja
            d = min(d_lista)
            print("Nije moguce pogoditi metu sa zadanom brzinom.")
            print("Najmanja udaljenost od mete za zadanu brzinu je: {:.2f}m.".format(d))
            
            indeks = d_lista.index(d)
            theta = th_lista[indeks]

            #print(theta)

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
            self.init(self.v0,theta,self.x0,self.y0,self.dt )
            self.plot_trajectory()
            self.reset()