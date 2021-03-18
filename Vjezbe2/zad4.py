import matplotlib.pyplot as plt
import math
from kosi_hitac import crtaj_x_y_graf
from kosi_hitac import izracunaj_maks_visinu
from kosi_hitac import izracunaj_domet
from kosi_hitac import izracunaj_maks_brzinu
from kosi_hitac import provjeri_metu

crtaj_x_y_graf(50,30,25)
izracunaj_maks_visinu(50,30,25)
izracunaj_domet(50,30,25)
izracunaj_maks_brzinu(50,30,25)
provjeri_metu(50,30,25,150,35,0.5)


#while True:
    #p_b = input("Unesite iznos pocetne brzine u metrima po sekundi: ")
    #try:
        #v0 = float(p_b)
        #break
    #except ValueError:
        #print("Iznos pocetne brzine mora biti broj, ponovite unos!")

#while True:
    #k_o = input("Unesite iznos kuta otklona pocetne brzine u stupnjevima: ")
    #try:
        #kut = float(k_o)
        #th = math.pi*kut/180
        #break
    #except ValueError:
        #print("Iznos kuta otklona mora biti broj, ponovite unos!")

#while True:
    #vrijeme = input("Unesite vrijeme kroz koje se odvija gibanje u sekundama: ")
    #try:
        #t = float(vrijeme)
        #break
    #except ValueError:
        #print("Vrijeme mora biti broj, ponovite unos!")

#while True:
    #metax = input("Unesite x koordinatu mete: ")
    #try:
        #xm = float(metax)
        #break
    #except ValueError:
        #print("Koordinata mora biti broj, ponovite unos!")

#while True:
    #metay = input("Unesite y koordinatu mete: ")
    #try:
        #ym = float(metay)
        #break
    #except ValueError:
        #print("Koordinata mora biti broj, ponovite unos!")

#while True:
    #radijus = input("Unesite radijus mete: ")
    #try:
        #r = float(radijus)
        #break
    #except ValueError:
        #print("Radijus mora biti broj, ponovite unos!")
