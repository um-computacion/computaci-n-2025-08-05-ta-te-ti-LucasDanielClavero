#posicion ocupada anteriormente
class PosOcupadaException(Exception):
    def __init__(self, mensaje="Esa posición ya está ocupada, elija otra."):
        super().__init__(mensaje)

#ingreso de coordenadas erroneas
class PosicionInvalidaException(Exception):
    def __init__(self, mensaje="Posición fuera del tablero, introdusca otra."):
        super().__init__(mensaje)

#ingreso de letras
class CaracterNoNumericoException(Exception):
    def __init__(self, mensaje="Debe ingresar un número unicamente"):
        super().__init__(mensaje)
