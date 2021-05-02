#include <iostream>

void ispisi_listu(int lista[], int n) {
    for(int i = 0; i < n; i++) {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;  
}

void ispis_u_intervalu(int lista[], int n, int a, int b) {
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << " ";
        }
        else {
            continue;
        } 
    } 
        std::cout << std::endl;
}   

void obrnuti_redosljed(int lista[], int n)  {
    int lista_1[n] = {};
    for (int i = 0; i < n; i++) {
        int k = lista[n - 1 - i];
        lista_1[i] = k; 
    }
    ispisi_listu(lista_1,n);
}

void zamjeni_clanove(int lista[], int n, int c, int d) {
    int e = lista[c-1];
    lista[c-1] = lista[d-1];
    lista[d-1] = e;
    //ispisi_listu(lista,n);
}

void sortiraj(int lista[], int n) {   // radi, ali ne dobro
    //for (int j = 0; j < n; j++) {
    //int j;
    //while (j < n-1) {
        for (int i = 0; i < n; i++) {
            if (lista[i] > lista[i+1]) {
                zamjeni_clanove(lista,n,i+1,i);
            }
        }
    //    j++;
    //}
    ispisi_listu(lista,n);
}

int main() {
    const int n = 5;
    int moja_lista[n] = {1,3,5,2,4};
    ispisi_listu(moja_lista,n);
    ispis_u_intervalu(moja_lista,n,2,7);
    sortiraj(moja_lista,n);  // ne radi
    obrnuti_redosljed(moja_lista,n);
    zamjeni_clanove(moja_lista,n,5,3);
    ispisi_listu(moja_lista,n);
    return 0;
}