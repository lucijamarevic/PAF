import Projectile as ptl 
import numpy as np

p = ptl.Projectile()

p.init(10,10,60,0,0,1.2,0.1,0.5,0.01)      #(m,v0,theta,x0,y0,ro,cd,A,dt)
p.move()
p.plot_trajectory()
p.reset()
p.move_ar()
p.plot_trajectory()