import gravity as g
import numpy as np
import matplotlib.pyplot as plt

ms =  1.989 * (10**30)
mz =  5.9742 * (10**24)
vs = np.array((0,0))
rs = np.array((0,0))
vz = np.array((0,29783))
rz = np.array((1.486*(10**11),0))

p = g.Gravity()

#(m1,m2,r1,v1,r2,v2)
p.init(ms,mz,rs,vs,rz,vz)
p.interact(60*60*24*365.242)

plt.figure("Gravitacijska interakcija", figsize=(7,7))
plt.plot(p.x1_list,p.y1_list, c = "yellow", label = "Sunce")
plt.plot(p.x2_list,p.y2_list, c = "blue", label = "Zemlja")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()