import random
from cls_Stack import cls_Stack
# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
          ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
          ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
          ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]]


def validar_expresion(expresion):
    pila = cls_Stack()
    if not pila.isempty():
        raise ValueError("La pila debe estar vacía antes de utilizarse.")

    parejas = {")": "(", "]": "[", "}": "{"}
    es_valida = True

    for caracter in expresion:
        if caracter in "([{":
            pila.push(caracter)
        elif caracter in parejas:
            if pila.isempty() or pila.pop() != parejas[caracter]:
                es_valida = False
                break

    # Las aperturas pendientes indican que faltaron cierres.
    if not pila.isempty():
        es_valida = False

    # Dejar la pila vacía incluso cuando la expresión sea incorrecta.
    while not pila.isempty():
        pila.pop()

    if not pila.isempty():
        raise ValueError("La pila debe estar vacía al finalizar su uso.")

    return es_valida
