"""
Q. 03-05. Implemente las funciones de multiplicación (*) y división (/) de dos vectores
usando los métodos especiales __mul__ y __truediv__. Suponiendo que v1 es (30, 40)
y v2 es (10, 20), codifique para devolver el siguiente resultado como resultado
de la multiplicacióny división de dos vectores.
"""

class Vector2D:

    def __init__(self, v1, v2):
        self.n1 = v1
        self.n2 = v2
        pass

    def __mul__(self, other):
        mult1 = self.n1 * other.n1
        mult2 = self.n2 * other.n2
        return Vector2D(mult1, mult2)
        pass

    def __truediv__(self, other):
        div1 = self.n1 / other.n1
        div2 = self.n2 / other.n2
        return Vector2D(div1, div2)
        pass

if __name__ == '__main__' :
    v1 = Vector2D(30, 40)
    v2 = Vector2D(10, 20)
    c = v1 * v2
    print("El producto de  30 * 10 es ", c.n1)
    print("El producto de  40 * 20 es ", c.n2)
    pass

if __name__ == '__main__':
    v1 = Vector2D(30, 40)
    v2 = Vector2D(10, 20)
    c = v1 / v2
    print("La divisón de 30 / 10 es ", c.n1)
    print("La divisón de 40 / 20 es ", c.n2)
    pass