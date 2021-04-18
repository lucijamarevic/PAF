# modul radi za bilo koju silu koju korisnik moze definirati kao funkciju brzine, vremena i polozaja
import modul as m

def f1(v,x,t):
    return 10

p1 = m.Particle()
p1.init(f1,1,0,0,1,0.01)    #(func,m,x0,v0,total_time,dt)
p1.plot_trajectory()

def f2(v,x,t):
    k = 10
    return -k*x

p2 = m.Particle()
p2.init(f2,1,2,0,5,0.01)    #(func,m,x0,v0,total_time,dt)
p2.plot_trajectory()