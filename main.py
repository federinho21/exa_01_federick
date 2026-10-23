"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from Subrutinas import validar_expresion, repartir_cartas, jugar
from cls_Jugador import cls_Jugador

while True:
    print("\n1. validar una expresion")
    print("2. jugar buscando la reina de corazones")
    print("3. salir")
    opcion = input("elige una opcion: ").strip()

    if opcion == "1":
        expresion = input("ingrese una expresion matematica: ")
        es_valida, error = validar_expresion(expresion)
        if es_valida:
            print("la expresion esta bien escrita en cuanto al uso de agrupadores.")
        else:
            print("la expresion esta mal escrita:", error)
    elif opcion == "2":
        jugadores = [
            cls_Jugador("Ihann"),
            cls_Jugador("Bollolo"),
            cls_Jugador("Caballin"),
            cls_Jugador("Aymara"),
        ]
        repartir_cartas(jugadores)
        jugar(jugadores)
    elif opcion == "3":
        break
    else:
        print("opcion incorrecta, elige 1, 2 o 3.")
