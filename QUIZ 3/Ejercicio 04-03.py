"""
A continuación se muestra la implementación de una cola en python(queue).
¿Cuál será el resultado del siguiente código?
"""
class Queue:

    def __init__(self):
        self.cola = []

    def enqueue(self, dato):
        self.cola.append(dato)

    def dequeue(self):
        self.cola.pop(0)

    def __str__(self):
        return str(self.cola)


Cola = Queue()
items = [10 * i for i in range(1, 10)]  #Crea una lista, igual que el ejercicio anterior.
for item in items:                      #Recorre igual la lista
    Cola.enqueue(item)                  #Llama la función enqueue y agrega dato a la lista "cola" creada en la linea 20
    if (item // 10) % 2 == 0:
        Cola.dequeue()                  #En esta linea, llama a la funcion dequeue si el residuo de la división del
                                        #iterador entre 10 es cero.

print(Cola)