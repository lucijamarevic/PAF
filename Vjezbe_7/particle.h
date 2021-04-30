class Particle {
    
    private:

        double ti,xi,yi,vx,vy,kut;  //attributes
        double dt;
        double g = -9.81;
        double D,t;

        void evolve();


    public: 

        Particle(double v0, double theta, double x0, double y0, double step = 0.001);  //constructor
        //~Particle();  //destructor

        double range();
        double time();

};