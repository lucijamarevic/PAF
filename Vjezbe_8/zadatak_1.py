import Projectile as ptl 
import matplotlib.pyplot as plt

p = ptl.Projectile()

p.init(10,10,60,0,0,1.2,1,0.5,0.01)      #(m,v0,theta,x0,y0,ro,cd,A,dt)
x1,y1 = p.move()
p.reset()
p.init(10,10,60,0,0,1.2,0.5,0.5,0.01)
x2,y2 = p.move_ar()

plt.plot(x1,y1, label = "bez otpora zraka")
plt.plot(x2,y2, c = "red", label = "s otporom zraka")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Eulerova metoda")
plt.legend(loc = "upper right")
plt.show()