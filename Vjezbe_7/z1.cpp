#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

class Particle {

    public:

        double ti,xi,yi,vx,vy,kut;    //attributes
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
                D = yi;
                while (true) {
                    evolve();
                    if (yi > D) {
                        D = yi;
                    }
                    else {
                        continue;
                    }
                }
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
    std::cout << "Domet iznosi: " << p1.range() << "m." << std::endl;  // calling a method
    std::cout << "vrijeme iznosi: " << p1.time() << "s." << std::endl;  // calling a method
    return 0;
    }