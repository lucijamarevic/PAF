#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

class Particle {
    public:
            //float kut = theta*M_PI/180
            //double vx = v0*cos(kut)
            //double vy = v0*sin(kut)
            //jos triba definirat liste
            
        float vi;
        int theta;
        float xi;
        float yi;
        float dt;     

};  //ova zagrada zatvara klasu


int main() {
  Particle p1;  // kreiram objekt iz klase
  p1.theta = 30
    cout << p1.theta << endl;
  return 0;
}