from cls_Stack import cls_Stack


class cls_Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        # Cada jugador tiene su propia pila de naipes.
        self.partida = cls_Stack()
