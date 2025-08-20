import unittest
from modelo.jugador import Jugador
from modelo.tateti import Tateti
from modelo.excepciones import PosOcupadaException, PosicionInvalidaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.jugador_x = Jugador("Alice", "X")
        self.jugador_o = Jugador("Bob", "O")
        self.juego = Tateti(self.jugador_x, self.jugador_o)
    def test_turno_inicial_es_jugador_x(self):
        self.assertEqual(self.juego.obtener_turno_actual(), self.jugador_x)
    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.obtener_turno_actual(), self.jugador_o)
    def test_ocupar_posicion_valida(self):
        self.juego.ocupar_posicion(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
    def test_ocupar_posicion_invalida(self):
        with self.assertRaises(PosicionInvalidaException):
            self.juego.ocupar_posicion(3, 3)
    def test_ocupar_posicion_ocupada(self):
        self.juego.ocupar_posicion(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_posicion(0, 0)
    def test_cambio_de_turno_automatico_despues_de_ocupar(self):
        self.juego.ocupar_posicion(0, 0)
        self.assertEqual(self.juego.obtener_turno_actual(), self.jugador_o)
    def test_hay_espacios_libres_true(self):
        self.assertTrue(self.juego.hay_espacios_libres())
    def test_hay_espacios_libres_false(self):
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        for fila, col in jugadas:
            self.juego.ocupar_posicion(fila, col)
        self.assertFalse(self.juego.hay_espacios_libres())
    def test_ganador_por_fila(self):
        self.juego.tablero.contenedor = [
            ["X", "X", "X"],
            ["O", "", "O"],
            ["", "", ""]
        ]
        self.assertEqual(self.juego.obtener_ganador(), "X")

    def test_ganador_por_columna(self):
        self.juego.tablero.contenedor = [
            ["O", "X", ""],
            ["O", "X", ""],
            ["O", "", ""]
        ]
        self.assertEqual(self.juego.obtener_ganador(), "O")
    def test_ganador_por_diagonal_principal(self):
        self.juego.tablero.contenedor = [
            ["X", "", ""],
            ["O", "X", ""],
            ["", "", "X"]
        ]
        self.assertEqual(self.juego.obtener_ganador(), "X")
    def test_ganador_por_diagonal_secundaria(self):
        self.juego.tablero.contenedor = [
            ["", "", "O"],
            ["X", "O", ""],
            ["O", "", ""]
        ]
        self.assertEqual(self.juego.obtener_ganador(), "O")
    def test_sin_ganador_empate(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertIsNone(self.juego.obtener_ganador())
if __name__ == "__main__":
    unittest.main()
