import matplotlib.pyplot as plt
import numpy as np
import em_field as f

o = f.EmField()
o.init(1,1,np.array((0,0,0)),np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,1)),0.01)  #(m,q,r,v,E,B,dt)
#o.move(0.1)

#print("Akceleracije: ")
#print(o.a_lista)