import matplotlib.pyplot as plt
import numpy as np
import em_field as field

e = field.EmField()
#(m,q,r,v,E,B,dt)
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
e.move(20)

p = field.EmField()
#(m,q,r,v,E,B,dt)
p.init(1,1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
p.move(20)

ax = plt.axes(projection = "3d")
ax.plot3D(e.x_lista,e.y_lista,e.z_lista, c = "blue", label = "elektron")
ax.plot3D(p.x_lista,p.y_lista,p.z_lista, c = "red", label = "pozitron")
plt.legend()
plt.show()