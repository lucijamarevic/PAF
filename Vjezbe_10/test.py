import numpy as np

a_lista = []
b_lista = []
a = np.array((1,2,3))
a_lista.append(a)
b = np.array((3,2,1))
b_lista.append(b)
a_lista.append(np.array((2,4,6)))
b_lista.append(np.array((1,3,5)))

print(np.add(a,b))

c_lista = []
for i in range(2):
    c = np.dot(a_lista[i],b_lista[i])
    c_lista.append(c)
#d = np.cross(a,b)

print("skalarni pordukt: ")
print(c_lista)
#print("Vektorski produkt: ")
#print(d)

