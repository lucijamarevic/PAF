#include <iostream>
#include "harm_o.h"

int main() {
    HarmonicOscillator o1(0.1,5,0,0.5,10);  //(m,k,v0,x0,time,step = 0.001); 
    //std::cout << "Period iznosi: " << o1.period() << "s." << std::endl;  
    
    return 0;
    }