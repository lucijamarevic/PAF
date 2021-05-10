import bungee_jumping as bj 
import matplotlib.pyplot as plt

j1 = bj.BungeeJumping()

j1.init(70,20,0,100,50,1.35,1,1,0.01)    #(m,k,v0,h,l,ro,cd,A,dt)
j1.jump(30, False)

plt.plot(j1.t_list,j1.x_list)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf bez otpora zraka")
plt.show()

j1.reset()

j1.init(70,20,0,100,50,1.35,1,1,0.01)    #(m,k,v0,h,l,ro,cd,A,dt)
j1.jump(30)

plt.plot(j1.t_list,j1.x_list)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf s otporom zraka")
plt.show()