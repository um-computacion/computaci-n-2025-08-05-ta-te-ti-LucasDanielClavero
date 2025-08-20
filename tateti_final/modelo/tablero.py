from modelo.excepciones import PosOcupadaException, PosicionInvalidaException

class Tablero:
    def __init__(self):
     self.contenedor = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
     ]

    def ocupar_posicion(self, fil, col, ficha):
        if not (0 <= fil < 3 and 0 <= col < 3):
            raise PosicionInvalidaException()
        if self.contenedor[fil][col] != "":
            raise PosOcupadaException()
        self.contenedor[fil][col] = ficha

    def hay_espacios_libres(self):
        return any("" in fila for fila in self.contenedor)

    def __str__(self):
        filas = []
        for fila in self.contenedor:
            filas.append(" | ".join(c if c != "" else " " for c in fila))
        return "\n---------\n".join(filas)
