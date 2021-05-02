def zamjeni_clanove(lista,n,c,d):
    e = lista[c-1]
    lista[c-1] = lista[d-1]
    lista[d-1] = e

def sortiraj(lista,n):
    for j in range(n-1):
        for i in range(n-1):
            if lista[i]>lista[i+1]:
                zamjeni_clanove(lista,n,i+1,i+2)
            #print(f"{i+1}. ponavljanje: {lista}.")
        #print(f"{j}-{i}. ponavljanje: {lista}")
 
m_lista = [10,-3,2,5,-16,15,-5]
n = len(m_lista)
print(f"Lista: {m_lista}")
sortiraj(m_lista,n)
print(f"Sortirana lista: {m_lista}")
