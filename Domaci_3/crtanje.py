import matplotlib.pyplot as plt

with open('data.txt', 'r') as file:
    procitano = file.read()
    print(procitano)
    #print(type(procitano))
    #print(procitano.split('-'))
    lista = list(procitano)
    print(lista)
