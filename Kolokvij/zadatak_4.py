import vertikalni_hitac as vh 

p1 = vh.VertikalniHitac()
p1.init(10,10)    #(h0,v0)
print("Maksimalna dosegnuta visina iznosi: {:.2f}m".format(p1.max_height(0.01)))   #(dt)
print("Ukupno vrijeme trajanja gibanje iznosi: {:.2f}s".format(p1.total_time(0.05)))    #(dt)
