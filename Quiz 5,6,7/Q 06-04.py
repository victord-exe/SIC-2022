"""
Ejercicio lógico: en cada palabra, reemplace las letras por un número,
teniendo en cuenta que para cada palabra separada por un espacio
la suma de sus dígitos es un número al cuadrado
Encuentra el número representado por cada letra.
"""

from math import sqrt, floor
import time


def is_square_digitsum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if sqrt(s) == int(sqrt(s)):
        return True
    return False


def find_all_squares():
    sqrs = [[] for _ in range(5)]
    for i in range(1, floor(sqrt(10 ** 5)) + 1):
        n = i * i
        if not is_square_digitsum(n):
            continue
        s = str(n)
        if len(s) == 3 and s[1] != s[2]:
            continue
        if len(s) == 5 and s[2] != s[3]:
            continue
        if len(s) in [4, 5] and len(set(s)) != 4:
            continue
        sqrs[len(s) - 1].append(n)
    return sqrs


def promising(s, n, dic):
    for i in range(len(s)):
        digit = int(str(n)[i])
        for key, value in dic.items():
            if key == s[i] and value != digit:
                return False
            if value == digit and key != s[i]:
                return False
    return True


def solve(words, dic, squares):
    global solved
    if (len(words) == 0):
        solved = dic
    else:
        s = words[0]
        candidates = squares[len(s) - 1]
        for n in candidates:
            if promising(s, n, dic):
                newdic = dic.copy()
                for i in range(len(s)):
                    newdic[s[i]] = int(str(n)[i])
                solve(words[1:], newdic, squares)


def Main():
    squares = find_all_squares()
    words = ['A', 'TO', 'ALL', 'XMAS', 'MERRY']
    dic = {}

    solve(words, dic, squares)
    for word in words:
        print(word, end=": ")
        for c in word:
            print(solved[c], end="")
        print()


start = time.time()
solved = {}
Main()
end = time.time()
print("Tiempo transcurrido: ", end - start, " seconds")
