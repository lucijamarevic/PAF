#include "harm_o.h" 
#include <iostream> 
#include <fstream>   //za *.txt file
#include <string>  // nisan sigurna zasto
#include <string.h>  // za pretvaranje lista u stringove ako bude trebalo

int main() {
    HarmonicOscillator o1(0.1,10,0,0.5,5);   //(m,k,v0,x0,time,step)
    o1.oscillate();

    // spremanje u datoteku
    std::ofstream fw;  // ispisuje, ali ne dobro
    fw.open("data.txt", std::ios_base::app); //std::ofstream::out);
    if (fw.is_open())
        {
            int a = sizeof(o1.x_list);   
            for (int i = 0; i < a; i++) {  
                fw << o1.x_list[i];
            }
            // ako pokrecen kod vise puta, ne pise ispocetka, nego nastavlja
            
            int b = sizeof(o1.v_list);
            int c = sizeof(o1.a_list);
            int d = sizeof(o1.t_list);
        
        fw.close();
    }

    else {
        std::cout << "Unable to open file"; 
    }
    return 0;
}