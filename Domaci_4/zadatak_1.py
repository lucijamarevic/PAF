import projectile as ptl
import matplotlib.pyplot as plt

kocka = ptl.Projectile()
kocka.init(5,10,60,0,0,1,2,0.75,0.01,"kocka")    #(m,v0,theta,x0,y0,ro,cd,a,dt,tijelo = "kugla")

x,y = kocka.runge_kutta()

kugla = ptl.Projectile()
kugla.init(5,10,60,0,0,1,2,0.5,0.01)    #(m,v0,theta,x0,y0,ro,cd,a,dt,tijelo = "kugla")

x1,y1 = kugla.runge_kutta()

plt.plot(x,y, label = "kocka")
plt.plot(x1,y1, label = "kugla")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graf")
plt.legend()
plt.show()