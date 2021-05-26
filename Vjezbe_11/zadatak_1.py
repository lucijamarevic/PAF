import gravity as g
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array((0.5,0.5))
r1 = np.array((0,0))
v2 = np.array((0,0))
r2 = np.array((0,0))

p = g.Gravity()

#(m1,m2,r1,v1,r2,v2,dt = 0.01)
p.init(1,500,r1,v1,r2,v2)
p.interact(10)

plt.plot(p.x1_list,p.y1_list, label = "cestica 1")
plt.plot(p.x2_list,p.y2_list, label = "cestica 2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()