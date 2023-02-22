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

push(stack, str("Banana"))      #['Banana']
push(stack, str("Apple"))       #['Banana', 'Apple']
push(stack, str("Tomato"))      #['Banana', 'Apple', 'Tomato']

stack.pop()                     #['Banana', 'Apple']

push(stack, str("Strawberry"))  #['Banana', 'Apple', 'Strawberry']
push(stack, str("Grapes"))      #['Banana', 'Apple', 'Strawberry', 'Grapes']

stack.pop()                     #['Banana', 'Apple', 'Strawberry']

print(stack)                    #['Banana', 'Apple', 'Strawberry']
