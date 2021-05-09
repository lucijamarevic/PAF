import Projectile as ptl
import matplotlib.pyplot as plt
import numpy as np

def ovisnost_dometa_o_koeficijentu_trenja_Cd():
    D_lista = []
    D_rk_lista = []
    Cd_lista = list(np.linspace(0,5, num = 50))

    p = ptl.Projectile()

    for cd in Cd_lista:
        p.init(10,10,60,0,0,1.2,cd,0.5,0.01)      #(m,v0,theta,x0,y0,ro,cd,A,dt)
        D = p.range()
        D_lista.append(D)
        D_rk = p.range_r_k()
        D_rk_lista.append(D_rk)
        p.reset()

    plt.figure("Graf 1")
    plt.plot(Cd_lista,D_lista, linewidth=3, label = "Euler")
    plt.plot(Cd_lista,D_rk_lista, c="red", label = "Runge-Kutta")
    plt.xlabel("Koeficijent trenja Cd")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o koeficijentu trenja Cd")
    plt.legend()
    plt.show()

def ovisnost_dometa_o_masi():
    D_lista = []
    D_rk_lista = []
    m_lista = list(np.linspace(0.01,10, num = 500))

    p = ptl.Projectile()

    for m in m_lista:
        p.init(m,10,60,0,0,1.2,1,0.5,0.01)      #(m,v0,theta,x0,y0,ro,cd,A,dt)
        D = p.range()
        D_lista.append(D)
        D_rk = p.range_r_k()
        D_rk_lista.append(D_rk)
        p.reset()

    plt.figure("Graf 1")
    plt.plot(m_lista,D_lista, linewidth=3, label = "Euler")
    plt.plot(m_lista,D_rk_lista, c="red", label = "Runge-Kutta")
    plt.xlabel("Masa [kg]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o masi")
    plt.legend()
    plt.show()

ovisnost_dometa_o_koeficijentu_trenja_Cd()
ovisnost_dometa_o_masi()