#include <iostream>
#include <math.h>

using namespace std;

const int n = 5;
int lista[n] = {1,2,3,4,5};

void ispis_u_intervalu(unsigned a, unsigned b) {
    for(int i = 0; i < n; i++) {
        if (lista[i] < a && lista[i] < b) {
            cout << lista[i] << endl;
        }
        else {
            continue;
        }
    }
}

// izbacuje ovo

/* C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/
../lib/gcc/x86_64-w64-mingw32/8.1.0/../../../../x86_64-w64-mingw32/lib/../lib/
libmingw32.a(lib64_libmingw32_a-crt0_c.o):crt0_c.c:(.text.startup+0x2e): 
undefined reference to `WinMain'collect2.exe: error: ld returned 1 exit status */