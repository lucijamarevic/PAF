#include "harm_o.h" 
#include <iostream> 
#include <fstream>   //za *.txt file
#include <string>

int main() {
    HarmonicOscillator o1(0.1,10,0,0.5,5);   //(m,k,v0,x0,time,step)
    o1.oscillate();
    return 0;
}