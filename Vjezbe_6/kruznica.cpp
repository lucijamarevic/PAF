#include <iostream>
#include<math.h>

using namespace std;

void tocka_i_kruznica(double sx, double sy, double r, double tx, double ty) {
    double d = sqrt((sx - tx)*(sx - tx) + (sy - ty)*(sy - ty));

    if (d < r) {
        cout << "Tocka se nalazi unutar kruznice i njena udaljenost od kruznice iznosi: " << r-d << "." << endl;
    }

    if (d == r) {
        cout << "Tocka se nalazi tocno na kruznici i njena udaljenost od kruznice iznosi 0."  << endl;
    }

    if (d > r) {
        cout << "Tocka se nalazi izvan kruznice i njena udaljenost od kruznice iznosi: " << d-r << "." << endl;
    }
}


int main() {
    tocka_i_kruznica(0,0,2,3,2);
    return 0;
}