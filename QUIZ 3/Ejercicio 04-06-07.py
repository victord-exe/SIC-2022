"""
El siguiente es el código para el juego de combinación de números.
Si el máximo es 100 y el número es 51, ¿cuál es la salida de count?
"""
from random import randint


max = int(input("ingresa el numero maximo:\t"))
num = int(input("ingresar el numero de adivinansas: "))


cont = 0
low, high = 1, max

while low < high:
    mid = (low + high) // 2
    cont += 1
    if (mid == num):
        print(f"Su numero es {num}")
        break
    elif (mid > num):
        high = mid - 1
    else:
        low = mid + 1

print(f"Busco {cont} veces")  #La salida del contador es de 6

"""
Q. 04-07. En el código del juego de combinación de números, si el máximo es 100 y el número es 25,
¿cuál es el resultado del conteo?

Cuando el máximo es 100 y el número 25, el contador imprime un resultado de 2.
"""