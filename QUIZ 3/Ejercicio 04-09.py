"""
Si la nueva estantería tiene 10 compartimentos,
usa el siguiente código para averiguar qué libro hay en cada compartimento.
"""
import requests


class hash_table:
    def __init__(self):
        self.table = [None] * 127

    # Función hash
    def Hash_func(self, value):
        key = 0
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value):  # Metodo para ingresar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value

    def put(x, i):
        x.append(i)
        pass


table = hash_table()

books = [
    "The Litlle Prince",
    "The Old Man and The Sea",
    "The Beauty an The Beast",
    "The Last Leaf",
    "Alice in Wonderland"
]

for book in books:
    key = sum(map(ord, book))
    table.put(key, book)
for key in table.table.keys():
    print(key, table.table[key])
