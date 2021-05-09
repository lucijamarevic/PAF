import matplotlib.pyplot as plt

with open('data.txt', 'r') as file:
    content = file.readlines()
    x_str = (content[0].split(" "))
    v_str = (content[1].split(" "))
    a_str = (content[2].split(" "))
    t_str = (content[3].split(" "))
    del x_str[-1]
    del a_str[-1]
    x = []
    v = []
    a = []
    t = []
    for e in x_str:
        x.append(float(e))
    for e in v_str:
        v.append(float(e))
    for e in a_str:
        a.append(float(e))
    for e in t_str:
        t.append(float(e))

plt.plot(t,x)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("x-t graf")
plt.savefig("x-t graf")
plt.show()

plt.plot(t,v)
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf")
plt.savefig("v-t graf")
plt.show()

plt.plot(t,a)
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")
plt.title("a-t graf")
plt.savefig("a-t graf")
plt.show()