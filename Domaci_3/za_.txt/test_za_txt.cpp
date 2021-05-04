#include <iostream>
#include <fstream>
#include <string>

int main () { 
    
    std::string moj_string;
    moj_string = "Volim programiranje";
    std::ofstream file;
    file.open ("test.txt"); 
    if (file.is_open) {   //"a pointer to a bound function may only be used to call the function"
    file << moj_string << " ";
    file.close();
    }
    else {
        std::cout << "Unable to open file" << std::endl;
    }
    return 0;
}