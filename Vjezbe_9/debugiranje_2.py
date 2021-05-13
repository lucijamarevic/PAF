import bungee_jumping as bj 
import matplotlib.pyplot as plt

j1 = bj.BungeeJumping()

j1.init(70,20,0,100,50,1.35,1,1,0.01)    #(m,k,v0,h,l,ro,cd,A,dt)

print(j1.rp)   ## svi iksei su mi veci od njega i zato ne radi

j1.jump(10, False)