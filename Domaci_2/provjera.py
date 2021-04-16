import modul as m

def f(x,k):
    return -k*x

p1 = m.Particle()
for x in range(1,11):
    p1.init(f(x,10),0,0,10,0.01)     # (f,x0,v0,total_time,dt)
    print(p1.f)
    p1.reset()