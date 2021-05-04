#include "harm_o.h"
#include <iostream>
 
HarmonicOscillator::HarmonicOscillator(double m, double k, double v0, double x0, double time, double step)
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
        x_list.push_back(xi);
        v_list.push_back(vi);
        a_list.push_back(ai); 
        t_list.push_back(ti); 
    }

void HarmonicOscillator::oscillate()
    {
        while (ti < t) {
            move();
        }
    }

double HarmonicOscillator::period()  // ne valja
    {
        T = 0;
        while (true) {
            move();
            if (xi < 0) {
                //std::cout << xi << std::endl;
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