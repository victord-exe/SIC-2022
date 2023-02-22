"""
Q. 03-01. Diseñe un programa que reciba las coordenadas (x1, y1), (x2, y2) de dos puntos
usuario e imprima la distancia entre los dos puntos. Para hacer esto, implemente la función
la distancia (x1, y1, x2, y2).
Paura de codigo: consulte la ecuación para encontrar la distancia entre dos puntos.

"""
import math


def Dist_Dos_Puntos(p1, p2):
    d = math.sqrt(math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2))
    return f"La distancia entre los dos puntos dados es: {d} "


p1 = []
p2 = []

user = input("Usuario: ")

for i in range(0, 2):
    x = float(input("Introduzca las coordenadas de X1,Y1 --> "))
    p1.append(x)

for i in range(0, 2):
    x = float(input("Introduzca las coordenadas de X2,Y2 --> "))
    p2.append(x)

print(Dist_Dos_Puntos(p1, p2))
