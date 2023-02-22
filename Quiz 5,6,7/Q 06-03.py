"""
Diseñe un algoritmo que codifique la secuencia de Fibonacci empleando recursividad
"""

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = float(input("Introduzca un número "))

print(f"""
    Fibonacci de {n}:
    {fibonacci(n)}
""")