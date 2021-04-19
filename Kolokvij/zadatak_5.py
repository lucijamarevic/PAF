import matplotlib.pyplot as plt
import vertikalni_hitac as vh 

p1 = vh.VertikalniHitac()
p1.init(10,10)    #(h0,v0)

p1.move(0.01)    #(dt)
print("Maksimalna visina bez otpora zraka iznosi: {:.2f}".format(p1.max_height(0.01)))    #(dt)
print("Ukupno vrijeme bez otpora zraka iznosi: {:.2f}".format(p1.total_time(0.01)))    #(dt)

plt.figure("Vertikalni hitac")
fig = plt.subplot()
plt.subplot(2,2,1)
plt.plot(p1.t,p1.h)
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.title("h-t graf bez otpora zraka")
plt.subplot(2,2,2)
plt.plot(p1.t,p1.v)
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf bez otpora zraka")

p1.reset()

p1.air_resistance(2,2,0.01)    #(m,k,dt)
print("Maksimalna visina s otporom zraka iznosi: {:.2f}".format(p1.max_height_ar(2,2,0.01)))    #(m,k,dt)
print("Ukupno vrijeme s otporom zraka iznosi: {:.2f}".format(p1.total_time_ar(2,2,0.01)))    #(m,k,dt)

plt.subplot(2,2,3)
plt.plot(p1.t,p1.h, c = "orange")
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.title("h-t graf s otporom zraka")
plt.subplot(2,2,4)
plt.plot(p1.t,p1.v, c = "orange")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf s otporom zraka")
plt.subplots_adjust(hspace = 0.6, wspace = 0.4)
plt.show()