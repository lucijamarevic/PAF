#include <iostream>

void ispisi_listu(int lista[], int n) {  // radi
    for(int i = 0; i < n; i++) {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;  
}

void ispis_u_intervalu(int lista[], int n, unsigned a, unsigned b) {  // radi
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << " ";
        }
        else {
            continue;
        } } 
        std::cout << std::endl;
        }   

void obrnuti_redosljed(int lista[], int n)  {  // radi
    int lista_1[n] = {};
    for (int i = 0; i < n; i++) {
        int k = lista[n - 1 - i];
        lista_1[i] = k; 
    }
    ispisi_listu(lista_1,n);
}

void zamjeni_clanove(int lista[], int n, int c, int d) {  // radi
    int e = lista[c-1];  // element na mjestu c
    lista[c-1] = lista[d-1];  // zamjenim ga s elementom na d
    lista[d-1] = e; // zamjenim element na d s onim na c prije prve zamjene
    ispisi_listu(lista,n);
}

void sortiraj(int lista[], int n) {   // ne radi, vrati istu listu
    int lista_2 = {};
    int e = lista[0];
    for (int i = 1; i < n; i++) {
        int e = lista[i];
        if (e > e) {   // nema smisla, ali ne znam kako drugacije
            lista[i] = e;
        }
    }
    ispisi_listu(lista,n);
}

int main() {
    const int n = 5;
    int lista[n] = {1,5,2,4,6};
    ispisi_listu(lista,n);  // radi
    ispis_u_intervalu(lista,n,2,7);  // radi
    obrnuti_redosljed(lista,n);  // radi
    zamjeni_clanove(lista,n,5,3);  // radi
    sortiraj(lista,n);  // ne radi
    return 0;
}