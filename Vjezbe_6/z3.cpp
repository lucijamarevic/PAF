#include <iostream>

void ispisi_listu(int lista[]) {
    int n = sizeof(lista);  // tako dobijem broj elemenata
    for(int i = 0; i < n; i++) {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;  
}

void ispis_u_intervalu(int lista[], unsigned a, unsigned b) {
    int n = sizeof(lista);  // tako dobijem broj elemenata
    for(int i = 0; i < n; i++) {
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
    for (int i = 0; i < n; i++) {
        int k = lista[n - i];  // npr. za i = 3, uzet ce 3 element od kraja
        lista_1[i] = k;  
    }
    ispisi_listu(lista_1);
}

void zamjeni_clanove(int lista[], int c, int d) {
    int e = lista[c-1];  // nadem element na mjestu c
    lista[c-1] = lista[d-1];  // zamjenim ga s elementom na mjestu d
    // int e ide prije ovoga jer bi u suprotnom element od c vec bio zamjenjen elementom od d
    lista[d-1] = e; // zamjenim element na mjestu d s elementomo na mjestu c
    ispisi_listu(lista);
}

void sortiraj(int lista[]) {
    int n = sizeof(lista);
    int lista_2 = {};
    int e = lista[0];
    for (int i = 1; i < n; i++) {
        int e = lista[i];
        if (e > e) {
            lista[i] = e;
        }
    }
    ispisi_listu(lista);
}

int main() {
    const int n = 5;
    int lista[n] = {1,5,2,4,6};
    ispisi_listu(lista);
    ispis_u_intervalu(lista, 2,7);
    obrnuti_redosljed(lista);
    zamjeni_clanove(lista,5,3);
    sortiraj(lista);
    return 0;
}