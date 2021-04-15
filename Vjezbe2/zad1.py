import matplotlib.pyplot as plt

def grafovi(F,m,v0,x0):
    dt = 0.1
    t = []
    a = []
    v = [] 
    x = []

    for i in range(100):
        ti = dt*i
        t.append(ti)
        ai = F/m
        a.append(ai)
        if i == 0:
            vi = v0
            v.append(vi)
            xi = x0
            x.append(xi)
        else:
            vi = vi + ai*dt
            v.append(vi)
            xi = xi + vi*dt
            x.append(xi)

    plt.figure("Grafovi")
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
    plt.show()

grafovi(10,0.1,10,0)
