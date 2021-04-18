# modul radi za bilo koju silu koju korisnik moze definirati kao funkciju brzine, vremena i polozaja
import matplotlib.pyplot as plt
import modul as m

def f1(v,x,t):
    return 10

p1 = m.Particle()
p1.init(f1,1.5,0,0,1,0.01)    #(func,m,x0,v0,total_time,dt)
p1.plot_trajectory()

def f2(v,x,t):
    k = 10
    return -k*x

p2 = m.Particle()
p2.init(f2,1.5,2,0,5,0.01)    #(func,m,x0,v0,total_time,dt)
p2.plot_trajectory()

# cisto iz znatizelje i radi dodatne provjere
def f3(v,x,t):     
    a = 1
    return a*v*v

p3 = m.Particle()
p3.init(f3,2,0,1,1,0.01)    #(func,m,x0,v0,total_time,dt)
#p3.plot_trajectory()

def f4(v,x,t):     
    b = 3
    return b*t

p4 = m.Particle()
p4.init(f4,2,0,0,2,0.01)    #(func,m,x0,v0,total_time,dt)
#p4.plot_trajectory()

def f5(v,x,t):     
    a = 3
    b = 2
    return a*x + v*t*t

p5 = m.Particle()
p5.init(f5,5,1,1,2,0.01)    #(func,m,x0,v0,total_time,dt)
#p5.plot_trajectory()