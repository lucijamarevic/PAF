import matplotlib.pyplot as plt

with open('data.txt', 'r') as file:
    procitano = file.read()
    print(procitano)
    lista = list(procitano)
    print(lista)
