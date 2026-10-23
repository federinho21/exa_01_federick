import random
from time import sleep
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
        raise ValueError("la pila debe estar vacia antes de utilizarse.")

    parejas = {")": "(", "]": "[", "}": "{"}
    cierres = {"(": ")", "[": "]", "{": "}"}
    error = ""

    for posicion, caracter in enumerate(expresion, start=1):
        if caracter in cierres:
            pila.push(caracter)
        elif caracter in parejas:
            if pila.isempty():
                error = f"cierre '{caracter}' sin apertura en la posicion {posicion}."
                break
            apertura = pila.pop()
            if apertura != parejas[caracter]:
                error = f"se esperaba '{cierres[apertura]}' pero se encontro '{caracter}' en la posicion {posicion}."
                break

    if not error and not pila.isempty():
        error = f"falta cerrar '{pila.peek()}' con '{cierres[pila.peek()]}'."

    # limpio la pila incluso si encontre un error.
    while not pila.isempty():
        pila.pop()
    if not pila.isempty():
        raise ValueError("la pila debe estar vacia al finalizar su uso.")

    return not error, error


def repartir_cartas(jugadores):
    if len(jugadores) != 4:
        raise ValueError("se necesitan cuatro jugadores para repartir.")

    for jugador in jugadores:
        if not jugador.partida.isempty():
            raise ValueError("las pilas deben estar vacias antes del reparto.")

    disponibles = [carta for palo in baraja for carta in palo]

    # reparto una carta por jugador en cada ronda.
    while not all(jugador.partida.isfull() for jugador in jugadores):
        for jugador in jugadores:
            if not jugador.partida.isfull():
                carta = random.choice(disponibles)
                jugador.partida.push(carta)
                disponibles.remove(carta)


def jugar(jugadores):
    jugadas = [[] for jugador in jugadores]
    ganador = None
    corazones = []
    ancho = max(len(jugador.nombre) for jugador in jugadores) + 4
    print()
    print("".join(f"{jugador.nombre:<{ancho}}" for jugador in jugadores))
    primer_turno = True

    while ganador is None and any(not j.partida.isempty() for j in jugadores):
        for indice, jugador in enumerate(jugadores):
            if jugador.partida.isempty():
                continue

            # espero entre turnos, sin retrasar el inicio ni el final.
            if not primer_turno:
                sleep(2)
            primer_turno = False

            carta = jugador.partida.pop()
            jugadas[indice].append(carta)
            print(" " * (ancho * indice) + carta, flush=True)

            if carta == "QC":
                ganador = jugador
                corazones = [c for c in jugadas[indice] if c.endswith("C")]
                break

    if ganador is None:
        print("no hubo ganador: se agotaron las cartas.")
    else:
        print(f"ganador: {ganador.nombre}")
        print("corazones acumulados:", ", ".join(corazones))

    # las cartas sobrantes se descartan; no cuentan como jugadas.
    for jugador in jugadores:
        while not jugador.partida.isempty():
            jugador.partida.pop()
        if not jugador.partida.isempty():
            raise ValueError("las pilas deben quedar vacias al finalizar.")

    return ganador, corazones
