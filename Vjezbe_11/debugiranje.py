import gravity as g
import numpy as np
import matplotlib.pyplot as plt

m1 =  198.9
m2 =  597.42
v1 = np.array((0,0))
r1 = np.array((0,0))
v2 = np.array((0,29))
r2 = np.array((148.6,0))

p = g.Gravity()

#(m1,m2,r1,v1,r2,v2)
p.init(m1,m2,r1,v1,r2,v2)
p.interact(1)

plt.plot(p.x1_list,p.y1_list, c = "yellow", label = "1")
plt.plot(p.x2_list,p.y2_list, c = "blue", label = "2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
#plt.show()