#include <vector>

class HarmonicOscillator {

    private:
 
        double m,k,v0,x0,dt,t;
        double xi,vi,ai,ti;
        double T;
        vector<double> x_list;
        double v_list[1000];
        double a_list[1000];
        double t_list[1000];

        void move();

    public:
        HarmonicOscillator(double m, double k, double v0, double x0, double time, double step = 0.001); 

        void oscillate();  
        double period();
};