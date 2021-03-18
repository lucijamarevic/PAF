import matplotlib.pyplot as plt
import math

def crtaj_x_y_graf(v0,th,t):
    g = 9.81
    dt = t/1000
    kut = th*math.pi/180
    v0x = v0*math.cos(kut)
    v0y = v0*math.sin(kut)
    x = []
    y = []

    ti = 0
    xi = 0
    vy = v0y
    yi = 0
    x.append(xi)
    y.append(yi)

    for i in range(1000):
        ti = ti + dt
        xi = xi + v0x*dt
        vy = vy - g*dt
        yi = yi + vy*dt
        if yi >= 0:
            x.append(xi)
            y.append(yi)

    plt.figure("Graf")
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("x-y graf")
    plt.show() 

def izracunaj_maks_visinu(v0,th,t):
    g = 9.81
    dt = t/1000
    kut = th*math.pi/180
    v0y = v0*math.sin(kut)
    y = []

    ti = 0
    vy = v0y
    yi = 0
    y.append(yi)

    for i in range(1000):
        ti = ti + dt
        vy = vy - g*dt
        yi = yi + vy*dt
        if yi >= 0:
            y.append(yi)

    hm = max(y)
    print(f"Maksimalna visina koju tijelo postigne je: {hm}m.")

def izracunaj_domet(v0,th,t):
    g = 9.81
    dt = t/1000
    kut = th*math.pi/180
    v0x = v0*math.cos(kut)
    v0y = v0*math.sin(kut)
    x = []

    ti = 0
    xi = 0
    vy = v0y
    yi = 0
    x.append(xi)

    for i in range(1000):
        ti = ti + dt
        xi = xi + v0x*dt
        vy = vy - g*dt
        yi = yi + vy*dt
        if yi >= 0:
            x.append(xi)

    Domet = max(x)
    print(f"Domet iznosi: {Domet}m.")

def izracunaj_maks_brzinu(v0,th,t):
    g = 9.81
    dt = t/1000
    kut = th*math.pi/180
    v0x = v0*math.cos(kut)
    v0y = v0*math.sin(kut)
    v = []

    ti = 0
    vy = v0y
    yi = 0
    vi = math.sqrt((v0x**2) + (vy**2))
    v.append(vi)

    for i in range(1000):
        ti = ti + dt
        vy = vy - g*dt
        yi = yi + vy*dt
        if yi >= 0:
            vi = math.sqrt((v0x**2)+(vy**2))
            v.append(vi)

    vm = max(v)
    print(f"Maksimalna brzina iznosi: {vm}m/s")


def provjeri_metu(v0,th,t,sx,sy,r):
    g = 9.81
    dt = t/1000
    kut = th*math.pi/180
    v0x = v0*math.cos(kut)
    v0y = v0*math.sin(kut)
    d_meta = math.sqrt(sx**2 + sy**2)
    x = []
    y = []
    d = []
    xm = []
    ym = []

    ti = 0
    xi = 0
    vy = v0y
    yi = 0
    x.append(xi)
    y.append(yi)

    pogodena = False
    for i in range(1000):
        ti = ti + dt
        xi = xi + v0x*dt
        vy = vy - g*dt
        yi = yi + vy*dt
        if yi < 0:
            break
        x.append(xi)
        y.append(yi)
        d_tm = math.sqrt((sx-xi)**2 + (sy-yi)**2)
        if d_tm <= r:
            pogodena = True
            break
        else:
            d.append(d_tm)

            
    if pogodena:
        print("Projektil je pogodio metu.")
    else:
        d_min = min(d)
        print("Projektil ne pogodi metu.")
        print(f"Najmanja udaljenost projektila od mete: {d_min}m")

    for fi in range(3600):
        xmi = sx + r*math.cos(fi)
        ymi = sy + r*math.sin(fi)
        xm.append(xmi)
        ym.append(ymi)

    plt.figure("Putanja i meta")
    plt.plot(x,y)
    plt.plot(xm,ym)
    plt.show()
