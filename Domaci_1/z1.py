import particle as prt

p1 = prt.Particle()

p1.init(10,60,0,0,0.01)   #(v0,theta,x0,y0,dt)

print("Ukupno vrijeme trajanja gibanje iznosi: {:.2f}s".format(p1.total_time()))
print("Najveca ostvarena brzina iznosi: {:.2f}m/s".format(p1.max_speed()))

p1.velocity_to_hit_target(20,20,5)  ##(mx,my,r)
p1.reset()

p1.init(10,60,0,0,0.01)
p1.angle_to_hit_target(5,3,1)  ##(mx,my,r)