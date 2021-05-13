import bungee_jumping as bj 
import matplotlib.pyplot as plt

j1 = bj.BungeeJumping()

j1.init(70,20,0,100,50,1.35,1,1,0.01)    #(m,k,v0,h,l,ro,cd,A,dt)
j1.jump(10, False)

#fig = plt.subplot()
#plt.subplot(2,2,1)
plt.plot(j1.t_list,j1.x_list)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("x-t graf")
#plt.subplot(2,2,2)
#plt.plot(j1.t_list,j1.v_list)
#plt.xlabel("t [s]")
#plt.ylabel("v [m/s]")
#plt.title("v-t graf")
#plt.subplot(2,2,3)
#plt.plot(j1.t_list,j1.a_list)
#plt.xlabel("t [s]")
#plt.ylabel("a [m/s^2]")
#plt.title("a-t graf")
#plt.subplots_adjust(wspace = 0.4, hspace = 0.6)
plt.show()

# akceleracija stvara problem