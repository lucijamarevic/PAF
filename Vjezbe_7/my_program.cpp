#include <iostream>
#include "particle.h"

int main() {
    Particle p1(10,45,0,0);  // creating an object, step by default (v0,theta,x0,y0,step)
    std::cout << "Domet iznosi: " << p1.range() << "m." << std::endl;  // calling a method
    std::cout << "vrijeme iznosi: " << p1.time() << "s." << std::endl;  // calling a method

    Particle p2(100,30,0,0);
    std::cout << "Domet iznosi: " << p2.range() << "m." << std::endl;
    std::cout << "vrijeme iznosi: " << p2.time() << "s." << std::endl;

    Particle p3(20,60,0,0);
    std::cout << "Domet iznosi: " << p3.range() << "m." << std::endl;
    std::cout << "vrijeme iznosi: " << p3.time() << "s." << std::endl;
    
    return 0;
    }