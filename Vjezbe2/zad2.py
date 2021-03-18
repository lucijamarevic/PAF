import matplotlib.pyplot as plt
import math

def grafovi_k_h(v0,th):
    g = 9.81
    dt = 0.1
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

    plt.figure("Grafovi")
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
    plt.subplots_adjust(wspace = 0.4, hspace = 0.6, bottom = 0.1)
    plt.show()

grafovi_k_h(50,45)
