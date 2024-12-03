import os, sys


def funcion_ejemplo():
    print("Hola, Mundo!")
    x = {"clave": "valor"}
    y = [1, 2, 3, 4, 5]
    z = (10, 20, 30)
    if x["clave"] == "valor":
        print("La clave es valor")
    for numero in y:
        print(numero)
    return x, y, z


funcion_ejemplo()
