class Jugador:
    def __init__(self, nombre: str, simbolo: str):
        self.nombre = nombre      
        self.simbolo = simbolo    # "X" o "O"

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_simbolo(self) -> str:
        return self.simbolo

    def __str__(self):
        return self.nombre
