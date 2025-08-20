import unittest
from modelo.tablero import Tablero
from modelo.excepciones import PosOcupadaException, PosicionInvalidaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
    def test_tablero_se_inicializa_vacio(self):
        for fila in self.tablero.contenedor:
            self.assertEqual(fila, ["", "", ""])
    def test_ocupar_posicion_valida(self):
        self.tablero.ocupar_posicion(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")
    def test_ocupar_posicion_ya_ocupada(self):
        self.tablero.ocupar_posicion(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.ocupar_posicion(1, 1, "O")
    def test_ocupar_posicion_no_valida(self):
        with self.assertRaises(PosicionInvalidaException):
            self.tablero.ocupar_posicion(3, 3, "X")
    def test_hay_espacios_libres_true(self):
        self.assertTrue(self.tablero.hay_espacios_libres())
    def test_hay_espacios_libres_false(self):
        for i in range(3):
            for j in range(3):
                self.tablero.ocupar_posicion(i, j, "X")
        self.assertFalse(self.tablero.hay_espacios_libres())
    def test_str_tablero_vacio(self):
        esperado = "  |   |  \n---------\n  |   |  \n---------\n  |   |  "
        self.assertEqual(str(self.tablero), esperado)
    def test_str_tablero_con_fichas(self):
        self.tablero.ocupar_posicion(0, 0, "X")
        self.tablero.ocupar_posicion(1, 1, "O")
        self.tablero.ocupar_posicion(2, 2, "X")
        esperado = "X |   |  \n---------\n  | O |  \n---------\n  |   | X"
        self.assertEqual(str(self.tablero), esperado)
if __name__ == '__main__':
    unittest.main()
