#include <iostream>
#include <list>

void ispisi_listu(int lista[]) {
    int n = sizeof(lista);  // tako dobijem broj elemenata
    for(int i = 0; i = n-1; i++) {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;  
}

void ispis_u_intervalu(int lista[], unsigned a, unsigned b) {
    int n = sizeof(lista);  // tako dobijem broj elemenata
    for(int i = 0; i = n-1; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << " ";
        }
        else {
            continue;
        } } 
        std::cout << std::endl;
        }   

void obrnuti_redosljed(int lista[])  {
    int n = sizeof(lista);
    int lista_1[n] = {};
    for (int i = 0; i = n-1; i++) {
        int k = lista[n - i];  // npr. za i = 3, uzet ce 3 element od kraja
        lista_1[i] = k;  
    }
}

void zamjeni_clanove(int lista[], int c, int d) {
    int e = lista[c];  // nadem element na mjestu c
    lista[c] = lista[d];  // zamjenim ga s elementom na mjestu d
    // int e ide prije ovoga jer bi u suprotnom element od c vec bio zamjenjen elementom od d
    lista[d] = e; // zamjenim element na mjestu d s elementomo na mjestu c
}

int main() {
    const int n = 5;
    int lista[n] = {1,5,2,4,6};
    ispisi_listu(lista);
    ispis_u_intervalu(lista, 2,7);
    //obrnuti_redosljed(lista);
    zamjeni_clanove(lista,1,2);
    return 0;
}