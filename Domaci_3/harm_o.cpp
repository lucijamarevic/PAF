#include "harm_o.h"

HarmonicOscillator::HarmonicOscillator(double m, double k, double v0, double x0, double time, double step = 0.001)
    {
        ti = 0;
        dt = step;
        xi = x0;
        vi = v0;
        ai = m/k;
        t = time;
    }

void HarmonicOscillator::move() 
    {
        vi += ai*dt;
        xi += vi*dt;
        ai = (-k/m)*xi;
        ti += dt;    
        // jos triba dodat period
    }

void HarmonicOscillator::oscillate()
    {
        while (ti < t) {
            move();
        }
    }

double HarmonicOscillator::period()
    {
        T = 0;
        while (true) {
            move();
            if (xi < 0) {
                T = 0;
                break;
            }
        }    
        while (true) {
            move();
            T += dt;
            if (xi > 0) {
                break;
            }
        }
        return 2*T;
    }