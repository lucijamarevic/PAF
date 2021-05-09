#include "harm_o.h" 
#include <iostream> 
#include <fstream>
#include <string> 
#include <string.h> 

int main() {
    HarmonicOscillator o1(0.1,10,0,0.5,10.0,0.01);   //(m,k,v0,x0,time,step)
    o1.oscillate();

    /* spremanje u datoteku koju nije htjelo otvoriti pa radim s cout-om
    std::ofstream fw;
    fw.open("data.txt", std::ios_base::app);
    if (fw.is_open())           
        {    
            int a = sizeof(o1.x_list);   
            for (int i = 0; i < a; i++) {  
                fw << o1.x_list.at(i);
            }
            
            fw << "\n";

            int b = sizeof(o1.v_list);
            for (int j = 0; j < b; j++) {  
                fw << o1.v_list.at(j);
            }

            fw << "\n";

            int c = sizeof(o1.a_list);
            for (int k = 0; k < c; k++) {  
                fw << o1.v_list.at(k);
            }

            fw << "\n";

            int d = sizeof(o1.t_list);
            for (int l = 0; l < d; l++) {  
                fw << o1.v_list.at(l);
            }

            fw << "\n";
        fw.close();
    }

    else {
        std::cout << "Unable to open file"; 
    } */
    return 0;
}