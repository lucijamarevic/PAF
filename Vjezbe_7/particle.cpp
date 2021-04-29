#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <particle.h>

using namespace std;

Particle::Particle(double v0, double theta, double x0, double y0, double step);
{
    kut = theta*M_PI/180;
    vx = v0*cos(kut);
    vy = v0*sin(kut);
    ti = 0;
    dt = step;
    xi = x0;
    yi = y0;
}






    // iz pythona
    /*def reset(self):
        self.v0 = 0 
        self.theta = 0
        self.xi = 0
        self.yi = 0
        self.dt = 0
        self.x = []
        self.y = []
        self.kut = 0
        self.v0x = 0
        self.v0y = 0

    def __move(self):
        a = 9.81
        self.xi = self.xi + self.vx*self.dt
        self.vy = self.vy - a*self.dt
        self.yi = self.yi + self.vy*self.dt
        self.x.append(self.xi)
        self.y.append(self.yi)

    def range(self):
        while self.yi >= 0:
            self.__move()
        return max(self.x)

    def analiticki_domet(self):
        D = ((self.v0**2)*math.sin(2*self.kut))/9.81
        return D

    def total_time(self):
        t = 0
        while self.yi >= 0:
            self.__move()
            t = t + self.dt
        return t */