import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F,m,t):
    dt = t/100
    t = []
    a = []
    v = []
    x = []

    ai = F/m
    ti = 0
    vi = 0
    xi = 0
    t.append(ti)
    a.append(ai)
    v.append(vi)
    x.append(xi)
    
    for i in range(100):
        ti = ti +dt
        ai = F/m
        vi = vi + ai*dt
        xi = xi + vi*dt
        t.append(ti)
        a.append(ai)
        v.append(vi)
        x.append(xi)

    plt.figure("Jednoliko gibanje")
    fig = plt.subplot()
    plt.subplot(2,2,1)
    plt.plot(t,a) 
    plt.xlabel("t")
    plt.ylabel("a")
    plt.title("a-t graf")
    plt.subplot(2,2,2)
    plt.plot(t,v)
    plt.xlabel("t")
    plt.ylabel("v")
    plt.title("v-t graf")
    plt.subplot(2,2,3)
    plt.plot(t,x)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("x-t graf")
    plt.subplots_adjust(wspace = 0.4, hspace = 0.6, bottom = 0.1)
    #plt.show() - ide u drugu funkciju da bi se slike prikazale istovremeno

def kosi_hitac(v0,th,t):
    g = 9.81
    dt = t/100
    kut = th*math.pi/180
    v0x = v0*math.cos(kut)
    v0y = v0*math.sin(kut)
    t = []
    x = []
    y = []

    ti = 0
    xi = 0
    vy = v0y
    yi = 0
    t.append(ti)
    x.append(xi)
    y.append(yi)

    for i in range(100):
        ti = ti + dt
        xi = xi + v0x*dt
        vy = vy - g*dt
        yi = yi + vy*dt
        t.append(ti)
        x.append(xi)
        y.append(yi)

    plt.figure("Kosi hitac")
    fig = plt.subplot()
    plt.subplot(2,2,1)
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("x-y graf")
    plt.subplot(2,2,2)
    plt.plot(t,x)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("x-t graf")
    plt.subplot(2,2,3)
    plt.plot(t,y)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("y-t graf")
    plt.subplots_adjust(wspace = 0.4, hspace = 0.6, bottom = 0.1, left = 0.15)
    plt.show()
