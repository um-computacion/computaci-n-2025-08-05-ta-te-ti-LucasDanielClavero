import unittest
from modelo.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_jugador_con_nombre_y_simbolo_X(self):
        jugador = Jugador("Lucas", "X")
        self.assertEqual(jugador.obtener_nombre(), "Lucas")
        self.assertEqual(jugador.obtener_simbolo(), "X")
        self.assertEqual(str(jugador), "Lucas")
    def test_jugador_con_nombre_y_simbolo_O(self):
        jugador = Jugador("Juana", "O")
        self.assertEqual(jugador.obtener_nombre(), "Juana")
        self.assertEqual(jugador.obtener_simbolo(), "O")
        self.assertEqual(str(jugador), "Juana")
    def test_jugador_con_nombre_con_espacios(self):
        jugador = Jugador("Pepe", "X")
        self.assertEqual(jugador.obtener_nombre(), "Pepe")
        self.assertEqual(jugador.obtener_simbolo(), "X")
        self.assertEqual(str(jugador), "Pepe")
if __name__ == '__main__':
    unittest.main()
