import projectile as ptl
import matplotlib.pyplot as plt

p1 = ptl.Projectile()

p1.init(10,10,60,0,0,1,2,"kugla",1,0.001)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
p1.angle_to_hit_target(2.5,1,0.5)

p2 = ptl.Projectile()

p2.init(10,30,60,0,0,1,2,"kugla",1,0.001)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
p2.angle_to_hit_target(6,2,0.5)

p3 = ptl.Projectile()

p3.init(5,50,60,0,0,1,2,"kugla",1,0.001)    #(m,v0,theta,x0,y0,ro,cd,tijelo,a,dt)
p3.angle_to_hit_target(4,1,0.5)