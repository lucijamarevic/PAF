import projectile as ptl
import matplotlib.pyplot as plt

p1 = ptl.Projectile()

p1.init(10,10,28,0,0,1,2,"kugla",1,0.01)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
x,y = p1.runge_kutta()
plt.plot(x,y, label = "28°")

p2 = ptl.Projectile()

p2.init(10,30,18,0,0,1,2,"kugla",1,0.01)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
w,z = p2.runge_kutta()
plt.plot(w,z, label = "18°")

p3 = ptl.Projectile()

p3.init(5,50,7,0,0,1,2,"kugla",1,0.01)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
a,b = p3.runge_kutta()
plt.plot(a,b, label = "7°")

plt.legend()
plt.show() 