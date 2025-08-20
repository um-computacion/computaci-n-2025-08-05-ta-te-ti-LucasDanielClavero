from modelo.tablero import Tablero
from modelo.excepciones import PosOcupadaException, PosicionInvalidaException
from modelo.jugador import Jugador 

class Tateti:
    def __init__(self, jugador_x: Jugador, jugador_o: Jugador):
        self.jugador_x = jugador_x
        self.jugador_o = jugador_o
        self.turno = jugador_x  # empieza el jugador X
        self.tablero = Tablero()

    def ocupar_posicion(self, fila: int, columna: int):
        try:
            self.tablero.ocupar_posicion(fila, columna, self.turno.obtener_simbolo())
        except PosOcupadaException as e:
            raise e
        except PosicionInvalidaException as e:
            raise e

        self.cambiar_turno()

    def cambiar_turno(self):
        self.turno = self.jugador_o if self.turno == self.jugador_x else self.jugador_x

    def hay_espacios_libres(self) -> bool:
        return self.tablero.hay_espacios_libres()

    def obtener_ganador(self):
     tablero = self.tablero.contenedor  

    # Verificar filas
     for fila in tablero:
        if fila[0] != " " and fila[0] == fila[1] == fila[2]:
            return fila[0]

    # Verificar columnas
     for col in range(3):
        if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
            return tablero[0][col]

    # Verificar diagonales
     if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return tablero[0][0]
     if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[0][2]

    # Si no hay ganador
     return None


    def obtener_turno_actual(self) -> Jugador:
        return self.turno

    def __str__(self):
        return str(self.tablero)
