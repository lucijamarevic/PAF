import matplotlib.pyplot as plt

def graf_akceleracije(F,m,):
    x = []
    y = []
    a = F/m
    y.append(a)
    t = list(range(1,11))
    for item in t:
        fl = float(item)
        x.append(fl)
    plt.plot(x,y)
    plt.xlabel(" t ")
    plt.ylabel(" a ")
    plt.title(" a-t graf ")
    plt.show()
    
while True:
    sila = input("Unesite iznos sile u Newtonima: ")
    try :
        F = float(sila)
        break
    except ValueError:
        print("Iznos sile mora biti broj, ponovite unos! ")

while True:
    masa = input("Unesite iznos mase u kilogramima: ")
    try:
        m = float(masa)
        break
    except ValueError:
        print("Iznos mase mora biti broj, ponovite unos: ")

graf_akceleracije(F,m)