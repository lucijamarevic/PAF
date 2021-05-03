import projectile as pr
import numpy as np

p = pr.Projectile()

for dt in (np.linspace(0.001,0.1, num = 10)):
    p.init(0.1,10,60,0,0,1.2,0.1,0.5,dt)      #(m,v0,theta,x0,y0,ro,cd,A,dt)
    p.plot_trajectory()
    p.reset()