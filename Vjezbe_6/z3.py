def zamjeni_clanove(lista,n,c,d):
    e = lista[c-1]
    lista[c-1] = lista[d-1]
    lista[d-1] = e

def sortiraj(lista,n):
    for j in range(n):
        for i in range(n-1):
            if lista[i]>lista[i+1]:
                zamjeni_clanove(lista,n,i,i+1)
        print(f"Sortirana lista: {lista}")

m_lista = [5,4,3,2,1]
n = len(m_lista)
print(f"Lista: {m_lista}")
sortiraj(m_lista,n)
