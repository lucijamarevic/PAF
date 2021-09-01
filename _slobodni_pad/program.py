import matplotlib.pyplot as plt
import free_fall as ff

p1 = ff.Particle()

p1.init(0.1,0,10)  #dt ostavljam po defaultu
h,v,t = p1.move()

# h-t graf
plt.plot(t,h)
plt.title("h-t graf")
plt.xlabel("t")
plt.ylabel("h")
plt.show()

# v-t graf
plt.plot(t,v)
plt.title("v-t graf")
plt.xlabel("t")
plt.ylabel("v")
plt.show()