import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import em_field as field

def konstantno_polje(t):
    return 1

def vremenski_promjenjivo_polje(t):
    return t/10

e = field.EmField()
#(m,q,r,v,E,dt,func)
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,konstantno_polje)  
x,y,z = e.runge_kutta(10)

e.reset()

e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,vremenski_promjenjivo_polje) 
x_,y_,z_ = e.runge_kutta(10)

ax = plt.axes(projection = "3d")
ax.plot3D(x,y,z, label = "konstantno magnestko polje")
ax.plot3D(x_,y_,z_, label = "vremenski promjenjivo magnetsko polje")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("usporedba polja")
ax.view_init(30,30)
plt.legend(loc = "upper center")
plt.show()

p = field.EmField()
p.init(1,1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,vremenski_promjenjivo_polje)  
xp,yp,zp = p.runge_kutta(10)

ax = plt.axes(projection = "3d")
ax.plot3D(x_,y_,z_, label = "elektron")
ax.plot3D(xp,yp,zp, label = "pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("vremenski promjenjivo polje")
ax.view_init(30,30)
plt.legend(loc = "upper right")
plt.show()