import matplotlib.pyplot as plt
from math import pi,sin,cos,sqrt
from numpy import linspace

def kosi_hitac(v0,theta,x0,y0,dt):
    g = -9.81
    th = theta*pi/180
    vx = v0*cos(th)
    vy = v0*sin(th)
    x = x0
    y = y0
    t = 0
    t_list = []
    x_list = []
    y_list = []
    t_list.append(t)
    x_list.append(x0)
    y_list.append(y0)

    while y >= 0:
        vy += g*dt 
        y += vy*dt
        x += vx*dt
        t += dt
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

    plt.plot(x_list,y_list)
    plt.xlabel("x / [m]")
    plt.ylabel("y / [m]")
    plt.title("x-y graf")
    plt.show()

def maks_visina(v0,theta,y0,dt):
    g = -9.81
    th = theta*pi/180
    vy = v0*sin(th)
    y = y0
    y_list = []
    y_list.append(y0)

    while y >= 0:
        vy += g*dt 
        y += vy*dt
        y_list.append(y)
    
    return max(y_list)

def domet(v0,theta,x0,y0,dt):
    g = -9.81
    th = theta*pi/180
    vx = v0*cos(th)
    vy = v0*sin(th)
    x = x0
    y = y0
    t = 0
    x_list = []
    x_list.append(x0)

    while y >= 0:
        vy += g*dt 
        y += vy*dt
        x += vx*dt
        t += dt
        x_list.append(x)
        
    return max(x_list)

def maks_brzina(v0,theta,x0,y0,dt):
    g = -9.81
    th = theta*pi/180
    vx = v0*cos(th)
    vy = v0*sin(th)
    v = v0
    x = x0
    y = y0
    t = 0
    v_list = []
    v_list.append(v)

    while y >= 0:
        vy += g*dt
        v = sqrt((vx)**2 + (vy)**2) 
        y += vy*dt
        x += vx*dt
        t += dt
        v_list.append(v)

    v_abs_list = []
    for e in v_list:
        e2 = abs(e)
        v_abs_list.append(e2)
    
    return max(v_abs_list)

def meta(v0,theta,x0,y0,dt,r,mx,my):
    pogodena = False
    g = -9.81
    th = theta*pi/180
    vx = v0*cos(th)
    vy = v0*sin(th)
    x = x0
    y = y0
    d = sqrt((mx - x)**2 + (my - y)**2)
    t = 0
    d_list = []
    x_list = []
    y_list = []
    x_list.append(x0)
    y_list.append(y0)
    if d <= r:
        pogodena = True
    else:
        d_list.append(d-r)

    while y >= 0:
        vy += g*dt 
        y += vy*dt
        x += vx*dt
        d = sqrt((mx - x)**2 + (my - y)**2)
        x_list.append(x)
        y_list.append(y)
        if d <= r:
            pogodena = True
        else:
            t += dt
            d_list.append(d-r)

    if pogodena:
        print("Meta je pogodena!")
    else:
        print("Meta nije pogodena, najmanja udaljenost od mete iznosi: {:.2f}".format(min(d_list)))

    xm_list = []
    ym_list = []
    for phi in linspace(0,2*pi, num = 360):
        xm = mx + r+cos(phi)
        ym = my + r*sin(phi)
        xm_list.append(xm) 
        ym_list.append(ym)

    plt.plot(x_list,y_list)
    plt.plot(xm_list,ym_list, c = "orange")
    plt.xlabel("x / [m]")
    plt.ylabel("y / [m]")
    plt.title("Putanja i meta")
    plt.show()