import random
from Cetaceo import Cetaceo

lista_in = open("lista_cetacei.txt", "r").read().splitlines()
lista_in.pop(0) #la prima riga del file è un header

lista_cetacei = []
for i in lista_in:
    lista_cetacei.append(Cetaceo(i))

print(random.choice(lista_cetacei))

