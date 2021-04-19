import matplotlib.pyplot as plt
import vertikalni_hitac as vh 

p1 = vh.VertikalniHitac()
p1.init(10,10)    #(h0,v0)
p1.move(0.01)    #(dt)

plt.figure("Vertikalni hitac")
fig = plt.subplot()
plt.subplot(2,1,1)
plt.plot(p1.t,p1.h)
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.title("h-t graf")
plt.subplot(2,1,2)
plt.plot(p1.t,p1.v)
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf")
plt.subplots_adjust(hspace = 0.6)
plt.show()

