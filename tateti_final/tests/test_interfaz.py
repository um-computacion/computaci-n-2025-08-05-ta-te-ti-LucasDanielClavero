import unittest
from unittest.mock import patch
from interfaz.interfaz import main

class TestInterfaz(unittest.TestCase):
    @patch("builtins.input", side_effect=[
    "Jugador1", "Jugador2", 
    "a", "2",                
    "1", "1",                
    "1", "2",                
    "2", "2",                
    "1", "3",
    "3", "3"
    ])
    def test_caracter_no_numerico(self, mock_input):
        try:
           main()
        except Exception as e:
           self.fail(f"main() lanzó una excepción inesperada: {e}")
    @patch("builtins.input", side_effect=[
        "Jugador1", "Jugador2",
        "1", "1", 
        "1", "2",  
        "2", "2",  
        "1", "3",  
        "3", "3"   
    ])
    def test_ganador_jugador1(self, mock_input):
        try:
            main()
        except Exception as e:
            self.fail(f"main() lanzó una excepción inesperada: {e}")
    @patch("builtins.input", side_effect=[
        "Jugador1", "Jugador2",
        "1", "1",  
        "1", "2",  
        "1", "3",  
        "2", "1",  
        "2", "3",  
        "2", "2",  
        "3", "1",  
        "3", "3",  
        "3", "2"   
    ])
    def test_empate(self, mock_input):
        try:
            main()
        except Exception as e:
            self.fail(f"main() lanzó una excepción inesperada: {e}")
