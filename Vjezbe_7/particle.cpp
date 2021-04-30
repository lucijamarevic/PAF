#define _USE_MATH_DEFINES
#include <math.h>
#include "particle.h"

Particle::Particle(double v0, double theta, double x0, double y0, double step) //constructor
    {
        ti = 0;
        dt = step;
        xi = x0;
        yi = y0;
        kut = theta*M_PI/180;
        vx = v0*cos(kut);
        vy = v0*sin(kut);
    }

void Particle::evolve()
    {
        while (yi >= 0) {
            vx += 0.;
            vy += g*dt;

            xi += vx*dt;
            yi += vy*dt;

            ti += dt;
        }
    }

double Particle::range()
    {
        evolve();
        D = xi;
        return D;
    }

double Particle::time()
    {
        evolve();
        t = ti;
        return t;
    }