import matplotlib.pyplot as plt
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

    def init(self,m,v0,theta,x0,y0,ro,cd,A,dt):
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
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.ro = ro         # za akceleraciju
        self.cd = cd
        self.A = A
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

    def __move(self):
        a = 9.81
        self.x += + self.vx*self.dt
        self.vy -= a*self.dt
        self.y += + self.vy*self.dt
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        #self.vi = math.sqrt(self.vx**2 + self.vy**2)
        #self.v.append(self.vi)

    def move(self):
        while self.y >= 0:
            self.__move()
            self.t += self.dt
            self.t_list.append(self.t)

        return self.x_list, self.y_list

    def __ax(self,v):
        return -abs(self.vx*self.vx*self.ro*self.cd*self.A)/(2*self.m)

    def __ay(self,v):
        return -9.81-abs(self.vy*self.vy*self.ro*self.cd*self.A)/(2*self.m)

    def __move_ar(self):
        self.vx += self.ax*self.dt      # x-smjer
        self.x += self.vx*self.dt
        self.ax = self.__ax(self.vx)
        self.x_list.append(self.x)
        self.vx_list.append(self.vx)
        self.ax_list.append(self.ax)
        self.vy += self.ay*self.dt      #y-smjer
        self.y += self.vy*self.dt
        self.ay = self.__ay(self.vy)
        self.y_list.append(self.y)
        self.vy_list.append(self.vy)
        self.ay_list.append(self.ay)

    def move_ar(self):   
        while self.y >= 0:
            self.__move_ar()
            self.t += self.dt
            self.t_list.append(self.t)
        return self.x_list,self.y_list

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

        self.x_list.append(self.x)
        self.vx_list.append(self.vx)
        self.ax_list.append(self.ax)

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

        self.y_list.append(self.y)
        self.vy_list.append(self.vy)
        self.ay_list.append(self.ay)

    def runge_kutta(self):   
        while self.y >= 0:
            self.__runge_kutta()
            self.t += self.dt
            self.t_list.append(self.t)
        return self.x_list,self.y_list
        
    def plot_trajectory(self):
        plt.figure("Graf za trenutno stanje")
        plt.plot(self.x_list,self.y_list)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()

    def range(self):
        self.move() 
        return max(self.x)

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*self.kut))/9.81
        return D

    def total_time(self):
        self.move()
        return t

    def max_speed(self):
        self.move()
        return max(self.v)

    #def velocity_to_hit_target(self,mx,my,r):
    #    self.mx = mx
    #    self.my = my
    #    self.r = r
    #    d_list = []
    #    v_list = []

        # dio koji racunau brzinu
    #    pogodena = False
    #    for self.v0 in range(101):
    #        self.vx = self.v0*math.cos(self.kut)
    #        self.vy = self.v0*math.sin(self.kut)
    #        self.__move()
    #        D =  math.sqrt((self.mx-self.xi)**2 + (self.my-self.yi)**2) 
    #        if D <= self.r:
    #            pogodena = True
    #            break
    #        else: 
    #            d_list.append(D - self.r)
    #            v_list.append(self.v0)
        
    #    if pogodena:
    #        print("Potrebna brzina za pogoditi metu je: {:.2f}m/s".format(self.v0))

            # dio koji crta metu
    #        x = []
    #        y = []
    #        for fi in list(np.linspace(0,360, num = 3600)):    
    #            rad = fi*math.pi/180
    #            xi = self.mx + self.r*math.cos(rad)
    #            x.append(xi)
    #            yi = self.my + self.r*math.sin(rad)
    #            y.append(yi)
    #        plt.plot(x,y)

            # dio koji crta putanju
    #        self.init(self.v0,self.theta,self.x0,self.y0,self.dt )
    #        self.plot_trajectory()
    #        self.reset()

    #    else:
    #        d = min(d_list)
    #        print("Nije moguce pogoditi metu sa zadanim kutem.")
    #        print("Najmanja udaljenost od mete za zadani kut iznosti: {:.2f}".format(d))

    #        indeks = d_list.index(d)
    #        v = v_list[indeks]

            # dio koji crta metu
    #        x = []
    #        y = []
    #        for fi in list(np.linspace(0,360, num = 3600)):    
    #            rad = fi*math.pi/180
    #            xi = self.mx + self.r*math.cos(rad)
    #            x.append(xi)
    #            yi = self.my + self.r*math.sin(rad)
    #            y.append(yi)
    #        plt.plot(x,y)

            # dio koji crta putanju
    #        self.init(v,self.theta,self.x0,self.y0,self.dt )
    #        self.plot_trajectory()
    #        self.reset()
    
    #def angle_to_hit_target(self,mx,my,r):
    #    self.mx = mx
    #    self.my = my
    #    self.r = r
    #    d_lista = []
    #    th_lista = []

        # dio koji racuna kut
    #    pogodena = False
    #    for self.theta in range(91):
    #        self.kut = self.theta*math.pi/180
    #        self.vx = self.v0*math.cos(self.kut)
    #        self.vy = self.v0*math.sin(self.kut)
    #        self.__move()
    #        D =  math.sqrt((self.mx-self.xi)**2 + (self.my-self.yi)**2) 
    #        if D <= self.r:
    #            pogodena = True
    #            break
    #        else:
    #            d_lista.append(D - self.r)
    #            th_lista.append(self.theta)

    #    if pogodena:
    #        print("Potreban kut za pogoditi metu je: {}°".format(self.theta))
            
            # dio koji crta metu
    #        x = []
    #        y = []
    #        for fi in list(np.linspace(0,360, num = 3600)):    
    #            rad = fi*math.pi/180
    #            xi = self.mx + self.r*math.cos(rad)
    #            x.append(xi)
    #            yi = self.my + self.r*math.sin(rad)
    #            y.append(yi)
    #        plt.plot(x,y)

            # dio koji crta putanju
    #        self.init(self.v0,self.theta,self.x0,self.y0,self.dt )
    #        self.plot_trajectory()
    #        self.reset()
        
    #    else:      # ode nesto ne valja
    #        d = min(d_lista)
    #        print("Nije moguce pogoditi metu sa zadanom brzinom.")
    #        print("Najmanja udaljenost od mete za zadanu brzinu je: {:.2f}m.".format(d))
            
    #        indeks = d_lista.index(d)
    #        theta = th_lista[indeks]

            #print(theta)

            # dio koji crta metu
    #        x = []
    #        y = []
    #        for fi in list(np.linspace(0,360, num = 3600)):    
    #            rad = fi*math.pi/180
    #            xi = self.mx + self.r*math.cos(rad)
    #            x.append(xi)
    #            yi = self.my + self.r*math.sin(rad)
    #            y.append(yi)
    #        plt.plot(x,y)

            # dio koji crta putanju
    #        self.init(self.v0,theta,self.x0,self.y0,self.dt )
    #        self.plot_trajectory()
    #        self.reset()