import projectile as ptl
import matplotlib.pyplot as plt

kocka = ptl.Projectile()
kocka.init(5,10,60,0,0,1,1,"kocka",1,0.01)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)

x,y = kocka.runge_kutta()

kugla = ptl.Projectile()
kugla.init(5,10,60,0,0,1,2,"kugla",1,0.01)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)

x1,y1 = kugla.runge_kutta()

plt.plot(x,y, label = "kocka")
plt.plot(x1,y1, label = "kugla")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graf")
plt.legend()
plt.show()