"""
Q. 03-02. Un palíndromo es una oración, palabra o cadena que se lee igual al derecho o al revés.
Por ejemplo, reconocer, radar o la frase "anita lava la tina". Usemos una llamada recurisva para determinar
el palíndromo. Defina una función llamada is_palindrome y escriba un programa para que reciba una cadena del usuario
e imprima si el palíndromo es correcto o no.
Pauta de código: Llame a la funcion is_palindrome dentro de la función is_palindrome(funcion recurisva)
"""


def is_palindrome(p):
    esp = ' '
    for i in range(len(esp)):
        clean = p.replace(esp[i], "")  # Se quitan los espacios de la cadena para poder comparar.

    if clean == clean[::-1]:  # Se compara si las palabras son iguales (sin espacios)
        return "es un palíndromo"
    else:
        return "no es un palíndromo"


palabra = input("Introduzca una palabra u oración ")

print(f"La palabra {is_palindrome(palabra)} ")
