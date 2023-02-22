"""
La siguiente es la implementación de una pila en python. ¿Cuál será el resultado del siguiente código?
"""


def new_stack():
    stack1 = []
    return stack1


def push(stack, i):
    stack.append(i)


def pop(stack):
    return stack.pop


stack = new_stack()

items = [10*i for i in range (1, 10)]   #Crea una lista que contiene 10*i, siendo i un valor del i al 10
                                        # dado por el ciclo for.

for item in items:                      #Ciclo for que recorre la lista creada y verifica si el residuo de la divisón
    push(stack, item)                   #de los valores de la lista es cero.
    if (item//10) % 2 == 0:            
        stack.pop()                     #De serlo, entonces, ejecuta stack.pop() para sacar ese elemento de la pila

print (stack)