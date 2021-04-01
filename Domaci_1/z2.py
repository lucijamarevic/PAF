import matplotlib.pyplot as plt
import math 
import particle as prt

def ovisnost_dometa():
    theta_lista = []
    D_lista = [] 

    p1 = prt.Particle()
    
    for theta in range(91):
        p1.init(10,theta,0,0,0.01)
        D = p1.range()
        theta_lista.append(theta)
        D_lista.append(D)
        p1.reset()

    plt.figure("Graf 1")
    plt.plot(theta_lista,D_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o pocetnom kutu otklona")
    plt.show()

def ovisnost_vremena():
    theta_lista = []
    t_lista = []

    p1 = prt.Particle()

    for theta in range(91):
        p1.init(10,theta,0,0,0.01)
        t = p1.total_time()
        theta_lista.append(theta)
        t_lista.append(t)
        p1.reset()

    plt.figure("Graf 2")
    plt.plot(theta_lista,t_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Vrijeme trajanja [s]")
    plt.title("Ovisnost vremena trajanja o pocetnom kutu otklona")
    plt.show()

ovisnost_dometa()
ovisnost_vremena()