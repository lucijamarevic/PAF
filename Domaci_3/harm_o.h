#include <vector>

using std::vector;

class HarmonicOscillator {

    private:
 
        double m,k,v0,x0,dt,t;
        double xi,vi,ai,ti,a;
        double T;

        void move();

    public:
        HarmonicOscillator(double m, double k, double v0, double x0, double time, double step = 0.001); 
        
        vector<double>x_list;
        vector<double>v_list;
        vector<double>a_list;
        vector<double>t_list;
        int n;

        void oscillate();  
        double period();
};