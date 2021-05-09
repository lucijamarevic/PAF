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
        while (true) {
            vi += ai*dt;
            xi += vi*dt;
            ai = (-k/m)*xi;
            ti += dt;
            x_list.push_back(xi);
            v_list.push_back(vi);
            a_list.push_back(ai); 
            t_list.push_back(ti);
            if (ti > t) {
                break;
            }
        }
    int a = sizeof(x_list);   
    for (int i = 0; i < a; i++) {  
        std::cout << x_list.at(i) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;

    int b = sizeof(v_list);   
    for (int j = 0; j < b; j++) {  
        std::cout << v_list.at(j) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;

    int c = sizeof(a_list);   
    for (int k = 0; k < c; k++) {  
        std::cout << a_list.at(k) << " ";
    }
    std::cout << std::endl;
    std::cout << "\n" << std::endl;

    int d = sizeof(t_list);   
    for (int l = 0; l < d; l++) {  
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