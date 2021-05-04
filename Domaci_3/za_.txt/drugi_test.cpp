// nesto s interneta

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
  string vehiclesList[10] = { "value0", "value1", "value2","value3", "value4", "value5","value6", "value7","value8", "value9" };
  int arraySize = *(&vehiclesList + 1) - vehiclesList;
  try {
    ofstream fw("C:\\Users\\Korisnik\\Desktop\\PAF\\Domaci_3\\test.txt", //open file for writing
    std::ofstream::out);  //check if file was successfully opened for writing
    if (fw.is_open())  // ne radi, stalno izbacuje "problem with opening the file"
    {
      //store array contents to text file
      for (int i = 0; i < arraySize; i++) {
        fw << vehiclesList[i] << "\n";
      }
      fw.close();
    }
    else cout << "Problem with opening the file";
  }
  catch (const char* msg) {  // neman blage veze sta je ovo
    cerr << msg << endl;
  }
}