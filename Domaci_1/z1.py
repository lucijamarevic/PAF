import matplotlib.pyplot as plt
import math
import particle as prt
 
p1 = prt.Particle()

##init(self,v0,theta,x0,y0,dt)
p1.init(10,60,0,0,0.01) 

print("Ukupno vrijeme trajanja gibanje iznosi: {:.2f}s".format(p1.total_time()))
print("Najveca ostvarena brzina iznosi: {:.2f}m/s".format(p1.max_speed()))

##velocity_to_hit_target(self,mx,my,r)
p1.velocity_to_hit_target(20,20,5)

##angle_to_hit_target(self,mx,my,r)
p1.angle_to_hit_target(20,20,5)