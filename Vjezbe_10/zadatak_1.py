import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import em_field as field

e = field.EmField()
#(m,q,r,v,E,B,dt)
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
e.euler(20)

p = field.EmField()
#(m,q,r,v,E,B,dt)
p.init(1,1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
p.euler(20)

ax = plt.axes(projection = "3d")
ax.plot3D(e.x_lista,e.y_lista,e.z_lista, c = "blue", label = "elektron")
ax.plot3D(p.x_lista,p.y_lista,p.z_lista, c = "red", label = "pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()