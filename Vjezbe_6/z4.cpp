#include <iostream>

void rjesi_sustav(float a1, float b1, float c1, float a2, float b2, float c2) {
    /* iz prve jednaadzbe dobijemo x = (c1 - b1*y)/a1, 
    i kad uvrstimo u drugu y(b2 - b1*a2/a1) = c2 - c1*a2/a1 */
    float k_b = b2 - b1*a2/a1;
    float k_c = c2 - c1*a2/a1;
    float y = k_c/k_b;
    float x = (c1 - b1*y)/a1;

    std::cout << "x = " << x << ", a y = " << y << std::endl;
}
 
int main() {
    rjesi_sustav(1,3,5,2,4,6);
    return 0;
}