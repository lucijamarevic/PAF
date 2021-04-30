#include <iostream>
#include <list>

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
    for (int i = 0; i = n-1; i++) {
        int k = lista[n - i];  // npr. za i = 3, uzet ce 3 element od kraja
        lista_1[i] = k;  
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
    /* for (int i = 0; i = n-1; i++) {
        lista_1[i] = lista[i];
        std::cout << lista_1[i] << " ";
    } 
    std::cout << std::endl;  */
}

//void zamjeni_clanove(lista)

int main() {
    const int n = 5;
    int lista[n] = {1,5,2,4,6};
    ispis_u_intervalu(lista, 2,7);
    obrnuti_redosljed(lista);
    return 0;
}