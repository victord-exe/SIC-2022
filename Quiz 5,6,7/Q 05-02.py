"""
¿Cuántas comparaciones se ejecutaron en el siguiente proceso de clasificación por inserción?
"""

"""
def insertionsort2(S):
    n = len(S)
    cont = 0  # Inicializo contador
    for i in range(1, n):
        comp = False
        print(S)
        x = S[i]
        j = i - 1

        while j >= 0 and S[j -1] > x:
            S[j] = S[j -1]
            j -= 1
            cont += 1
            comp = True
        S[j + 1] = x

        if comp == True:
            print(comp)
            cont += 1
    return cont


S = [50, 30, 40, 10, 20]

print(f"Se hicieron {insertionsort2(S)} comparaciones")

# La variable comp cambia a True si entra en el while y suma uno al contador
# Luego, agrego un if. Si entró al while, cont es True, no va a entrar al if.
# Si no entra al if, el ciclo for volvió a inicializar comp en False
# De modo que si no entra al while, entra al if y suma uno al contador
"""
def insertion_sort(array):

    cont = 0

    for i in range(1, len(array)):
        print(array)

        x = array[i]
        j = i

        cont += 1
        while j > 0 and array[j - 1] > x:
            array[j] = array[j -1]
            j = j - 1
            cont += 1
        array[j] = x

    return cont

array = [50, 30, 40, 10, 20]


print (insertion_sort(array))