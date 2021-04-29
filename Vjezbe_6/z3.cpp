#include <iostream>
#include <math.h>

using namespace std;

const int n = 5;
int lista[n] = {1,5,2,4,6};

void ispis_u_intervalu(unsigned a, unsigned b) {
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            cout << lista[i] << " ";
        }
        else {
            continue;
        } } 
        cout << endl;
        }   

void reverse_list()  {   // ne valja
    cout << "Obrnuti redosljed glasi: " << endl;
    int i,j,element;
    for (j = n - 1; j = 0; j--) {
        element = lista[j];
        for (i = 1; i < n; i++) {
        lista[i] = element;
        }
        cout << lista[i] << endl;
    }
}

int main() {
    ispis_u_intervalu(2,7);
    reverse_list();
    return 0;
}