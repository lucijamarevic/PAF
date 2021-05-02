#include <iostream>

void ispisi_listu(int lista[], int n) {
    for(int i = 0; i < n; i++) {
        std::cout << lista[i] << ", ";
    }
    std::cout << std::endl;  
}

void ispis_u_intervalu(int lista[], int n, int a, int b) {
    std::cout << "Elementi u intervalu od " << a << " do " << b << ":  ";
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << ", ";
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
    std::cout << "Obrnuti redosljed: " << " ";
    ispisi_listu(lista_1,n);
}

void zamjeni_clanove(int lista[], int n, int c, int d) {
    int e = lista[c-1];
    lista[c-1] = lista[d-1];
    lista[d-1] = e;
    //ispisi_listu(lista,n);
}

void sortiraj(int lista[], int n) {   // radi, ali ne dobro
    for (int j = 0; j < n-1; j++) {    
        for (int i = 0; i < n-1; i++) {
            if (lista[i] > lista[i+1]) {
                zamjeni_clanove(lista,n,i+1,i+2);
            }
        }
    }
    std::cout << "Sortirana lista: " << " ";
    ispisi_listu(lista,n);
}

int main() {
    const int n = 8;
    int moja_lista[n] = {5,-4,8,-10,15,-3,20,-13};
    ispisi_listu(moja_lista,n);
    ispis_u_intervalu(moja_lista,n,-10,10);
    obrnuti_redosljed(moja_lista,n);
    zamjeni_clanove(moja_lista,n,3,6);
    std::cout << "Zamjenjeni clanovi: " << " ";
    ispisi_listu(moja_lista,n);
    sortiraj(moja_lista,n);  // ne radi
    return 0;
}