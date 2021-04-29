class Particle {
    
    private:

        double ti,xi,yi,vx,vy;
        double dt;
        double g = -9.81;

        void evolve();


    public:

        Particle(double v0, double theta, double x0, double y0, double step = 0.001);
        ~Particle();

        double range();
        double time();

};