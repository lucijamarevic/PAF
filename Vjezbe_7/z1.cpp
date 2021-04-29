#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

class Particle {

    public:

        Particle(double v0, double theta, double x0, double y0, double step = 0.001);
        ~Particle()
        {
            double ti,xi,yi,vx,vy;
            double dt;
            double g = -9.81;

            ti = 0;
            dt = step;
            xi = x0;
            yi = y0;
            kut = theta*M_PI/180;
            vx = v0*cos(kut);
            vy = v0*sin(kut);
        }

        double range();
        double time();
    
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

};