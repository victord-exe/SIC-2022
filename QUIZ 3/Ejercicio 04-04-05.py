"""
¿Cuál es el algoritmo de la siguiente función find_two()?
Analice el código y escriba el resultado de la ejecución.
"""


def find_two(num):
    x = y = 0
    for i in range(1, len(num)):
        if num[x] < num[i]:
            x = i
        elif num[y] > num[i]:
            y = i
    return x, y


nums = [11, 37, 45, 26, 59, 28, 17, 53]
i, j = find_two(nums)
print(nums[i], nums[j])  # 59 11


"""
04-05. 
Cuántas comparaciones debe realizar la función find_two() implementada en la pregunta anterior (Q.04-04)?

debe realizar len(num) comparaciones, o sea, 8 comparaciones.
"""