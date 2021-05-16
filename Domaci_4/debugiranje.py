import projectile as ptl
import matplotlib.pyplot as plt
import math

p2 = ptl.Projectile()

p2.init(10,30,21,0,0,1,2,0.1,0.01)    #(m,v0,theta,x0,y0,ro,cd,a,dt,tijelo = "kugla")
p2.runge_kutta()
p2.plot_trajectory()

x = []
y = []
for fi in range(360):    
    rad = fi*math.pi/180
    xi = 6 + 0.5*math.cos(rad)
    x.append(xi)
    yi = 2 + 0.5*math.sin(rad)
    y.append(yi)

plt.plot(x,y)
plt.show()