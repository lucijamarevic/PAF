
class VertikalniHitac:
    def init(self,h0,v0):
        self.h0 = h0
        self.v0 = v0
        
        print("Objekt je uspjesno storen.")
        print("Pocetna visina iznosi: {:.2f}m, a pocetna brzina: {:.2f}m/s".format(h0,v0))

    def change_height(self,novi_h0):
        self.h0 = novi_h0
        print("Nova pocetna visina iznosi: {:.2f}m".format(self.h0))

    def change_speed(self,novi_v0):
        self.v0 = novi_v0
        print("Nova pocetna brzina iznosi: {:.2f}m/s".format(self.v0))