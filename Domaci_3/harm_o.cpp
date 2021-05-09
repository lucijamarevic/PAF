#include "harm_o.h"
#include <iostream>

using std::cout;
using std::endl;
 
HarmonicOscillator::HarmonicOscillator(double m, double k, double v0, double x0, double time, double step)
    {
        k = k;
        m = m;
        ti = 0;
        xi = x0;
        vi = v0;
        a = -k/m;
        ai = a*xi;
        t = time;
        dt = step;
        n = t/dt;
        x_list.push_back(xi);
        v_list.push_back(vi);
        a_list.push_back(ai); 
        t_list.push_back(ti);
    }

void HarmonicOscillator::move()
    {
        vi = vi + ai*dt;
        xi = xi + vi*dt;
        ai = a*xi;
        ti += dt;
        x_list.push_back(xi);
        v_list.push_back(vi);
        a_list.push_back(ai); 
        t_list.push_back(ti);
    }

void HarmonicOscillator::oscillate()
    {
        for (int i = 0; i < n ; i++)
        {
            move();
        }

    for (int i = 0; i < n; i++) {  
        cout << x_list.at(i) << " ";
    }
    cout << endl;
 
    for (int j = 0; j < n; j++) {  
        cout << v_list.at(j) << " ";
    }
    cout << endl;
  
    for (int k = 0; k < n; k++) {  
        cout << a_list.at(k) << " ";
    }
    cout << endl;
  
    for (int l = 0; l < n; l++) {  
        cout << t_list.at(l) << " ";
    }
    cout << endl;
    }

double HarmonicOscillator::period()
    {
        T = 0;
        while (true) {
            oscillate();
            if (xi < 0) {
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