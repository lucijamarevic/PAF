def three_step(func,x,h):
    return (func(x+h) - func(x-h)) / (2*h)

def two_step(func,x,h):
    return (func(x+h) - func(x)) / h

def derivative(func,a,b,h,m = 3):  
    xlista = []
    ylista = []
    x = a
    while x <= b:    #x ide od a do b
        xlista.append(x)
        x += h

    if m == 2:    #ako korisnik unese 2, ide two_step
        for x in xlista:
            d = two_step(func,x,h)
            ylista.append(d)
    elif m == 3:         #ako korisnik ne unese 2, ide three_step
        for x in xlista:    
            d = three_step(func,x,h)
            ylista.append(d)

    return xlista,ylista

def integrate_rectangle(func,a,b,n):
    dx = (b-a)/n 
    gornja_meda = 0
    donja_meda = 0
    c = a + dx    #za gornju medu pocinjemo od x1
    d = a    #za donju medu pocinjemo od x0
    for i in range(n):
        gornja_meda += func(c)*dx
        c += dx
        donja_meda += func(d)*dx
        d += dx
    
    return gornja_meda, donja_meda
    
def integrate_trapeze(func,a,b,n):
    dx = (b-a)/n
    suma = 0
    x = a
    for i in range(n):
        suma += func(x)
        x += dx
    integral = suma*dx + ((func(b) + func(a))/2)*dx
    
    return integral