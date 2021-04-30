#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

class Particle {

    public:

        double ti,xi,yi,vx,vy,kut;  //attributes
        double dt;
        double g = -9.81;
        double D,t;

        Particle(double v0, double theta, double x0, double y0, double step = 0.001)  //constructor
        {
            ti = 0;
            dt = step;
            xi = x0;
            yi = y0;
            kut = theta*M_PI/180;
            vx = v0*cos(kut);
            vy = v0*sin(kut);
        }

        double range()
            {
                evolve();
                    D = xi;
                return D;
            }

        double time()
        {
            evolve();
            t = ti;
            return t;
        }
    
    private:

        void evolve()
        {
            while (yi >= 0) {
                vx += 0.;
                vy += g*dt;

                xi += vx*dt;
                yi += vy*dt;

                ti += dt;
            }
        }

};  //end of class

int main() {
    Particle p1(10,60,0,0);  // creating an object, step by default (v0,theta,x0,y0,step)
    double D = p1.range();
    double t = p1.time(); 
    std::cout << "Domet iznosi: " << D << "m." << std::endl;  // calling a method
    std::cout << "vrijeme iznosi: " << t << "s." << std::endl;  // calling a method

    Particle p2(100,45,0,0);  // creating an object, step by default (v0,theta,x0,y0,step)
    double D2 = p2.range();
    double t2 = p2.time(); 
    std::cout << "Domet iznosi: " << D2 << "m." << std::endl;  // calling a method
    std::cout << "vrijeme iznosi: " << t2 << "s." << std::endl;  // calling a method

    Particle p3(50,30,0,0);  // creating an object, step by default (v0,theta,x0,y0,step)
    double D3 = p3.range();
    double t3 = p3.time(); 
    std::cout << "Domet iznosi: " << D3 << "m." << std::endl;  // calling a method
    std::cout << "vrijeme iznosi: " << t3 << "s." << std::endl;  // calling a method
    return 0;
    }