"""
¿Cuántas comparaciones se ejecutaron en el siguiente proceso de clasificación por inserción?
"""


def bubbleSort(arr):
    n = len(arr)
    cont = 0 #Inicializo un contador
    for i in range(n - 1):
        print(arr)

        for j in range(0, n - i - 1):
            cont += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return cont

arr = [50, 30, 40, 10, 20]

print(f"se hicieron { bubbleSort(arr) } comparaciones")
