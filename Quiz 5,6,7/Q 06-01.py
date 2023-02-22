"""
Diseñe un algoritmo que halle la función factorial de cualquier número empleando recursividad
"""

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Ingrese un número entero mayor a cero -> "))

while num <= 0:
    print("*** ERROR ***")
    num = int(input("Ingrese de nuevo un número entero -> "))

result = factorial(num)
print(f"El factorial de {num} es {result}")