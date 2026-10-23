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
from Subrutinas import validar_expresion, repartir_cartas
from cls_Jugador import cls_Jugador

expresion = input("Ingrese una expresión matemática: ")

if validar_expresion(expresion):
    print("La expresión está bien escrita en cuanto al uso de agrupadores.")
else:
    print("La expresión está mal escrita en cuanto al uso de agrupadores.")

# cada jugador crea su propia pila desde el constructor.
jugadores = [
    cls_Jugador("Ihann"),
    cls_Jugador("Bollolo"),
    cls_Jugador("Caballin"),
    cls_Jugador("Aymara"),
]

repartir_cartas(jugadores)

