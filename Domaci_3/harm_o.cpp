#include "harm_o.h"
#include <iostream>
 
HarmonicOscillator::HarmonicOscillator(double m, double k, double v0, double x0, double time, double step)
    {
        ti = 0;
        xi = x0;
        vi = v0;
        ai = m/k;
        t = time;
        dt = step;
    }

void HarmonicOscillator::oscillate()
    {
        int n = t/dt;
        for (int i = 0; i < n ; i++)
        {
            vi = vi + ai*dt;
            xi = xi + vi*dt;
            ai = (-k/m)*xi;
            ti += dt;
            x_list.push_back(xi);
            v_list.push_back(vi);
            a_list.push_back(ai); 
            t_list.push_back(ti);
        }
 
    for (int i = 0; i < n; i++) {  
        std::cout << x_list.at(i) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;
 
    for (int j = 0; j < n; j++) {  
        std::cout << v_list.at(j) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;
  
    for (int k = 0; k < n; k++) {  
        std::cout << a_list.at(k) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;
  
    for (int l = 0; l < n; l++) {  
        std::cout << t_list.at(l) << " ";
    }
    std::cout << std::endl;
    }

double HarmonicOscillator::period()  // ne valja
    {
        T = 0;
        while (true) {
            oscillate();
            if (xi < 0) {
                //std::cout << xi << std::endl;
                break;
            }
        }    
        while (true) {
            oscillate();
            T += dt;
            if (xi > 0) {
                break;
            }
        }
        return 2*T;
    }