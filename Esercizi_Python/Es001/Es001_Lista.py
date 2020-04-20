import math

lista = []
while(1):
    x = int(input("Insert a number: "))
    if(math.isnan(x)):
        break
    else:
        lista.append(x)

print(f"Lista = {lista}")