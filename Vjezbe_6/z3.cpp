#include <iostream>
#include <list>

const int n = 5;
int lista[n] = {1,5,2,4,6};

void ispis_u_intervalu(unsigned a, unsigned b) {
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            std::cout << lista[i] << " ";
        }
        else {
            continue;
        } } 
        std::cout << std::endl;
        }   

void reverse_list()  {   // ne valja
    std::cout << "Obrnuti redosljed glasi: " << std::endl;
    std::list<int> lista;
    lista.reverse();
    for (std::list<int>::iterator it=lista.begin(); it!=lista.end(); ++it)
        std::cout << ' ' << *it;
    std::cout << '\n';
}

int main() {
    ispis_u_intervalu(2,7);
    reverse_list();
    return 0;
}