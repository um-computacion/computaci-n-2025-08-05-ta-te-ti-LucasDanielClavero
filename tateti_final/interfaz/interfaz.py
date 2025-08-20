import os
import time
from modelo.tateti import Tateti
from modelo.jugador import Jugador
from modelo.excepciones import PosicionInvalidaException, PosOcupadaException, CaracterNoNumericoException

def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia de usuario."""
    # Para Windows es 'cls', para Mac/Linux es 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # 1. BUCLE PRINCIPAL PARA REINICIAR EL JUEGO
    while True:
        limpiar_pantalla()
        print("--- ¡Bienvenido a una nueva partida de Ta-Te-Ti! ---")
        
        nombre1 = input("Ingrese el nombre del Jugador 1 (X): ")
        nombre2 = input("Ingrese el nombre del Jugador 2 (O): ")
        
        jugador_x = Jugador(nombre1, "X")
        jugador_o = Jugador(nombre2, "O")
        
        tateti = Tateti(jugador_x, jugador_o) 
        
        # Bucle para los turnos de una partida
        while True:
            limpiar_pantalla()
            print("\nTablero:")
            print(tateti)
            print(f"\nTurno de {tateti.turno.obtener_nombre()} ({tateti.turno.obtener_simbolo()})")
            
            try:
                fil_str = input("Ingrese la fila (1 a 3): ")
                col_str = input("Ingrese la columna (1 a 3): ")
                
                if not (fil_str.isdigit() and col_str.isdigit()):
                    raise CaracterNoNumericoException()
                
                fil = int(fil_str) - 1
                col = int(col_str) - 1
                
                tateti.ocupar_posicion(fil, col)
                ganador = tateti.obtener_ganador()
                
                # Si hay un ganador, se rompe el bucle de turnos
                if ganador:
                    limpiar_pantalla()
                    print("\nTablero final:")
                    print(tateti)
                    nombre_ganador = jugador_x.obtener_nombre() if ganador == jugador_x.obtener_simbolo() else jugador_o.obtener_nombre()
                    print(f"\n¡Ganó {nombre_ganador} ({ganador})!")
                    break # Sale del bucle de turnos
                
                # Si hay empate, también se rompe
                if not tateti.tablero.hay_espacios_libres():
                    limpiar_pantalla()
                    print("\nTablero final:")
                    print(tateti)
                    print("\n¡Empate! No hay más espacios libres.")
                    break # Sale del bucle de turnos

            except (PosicionInvalidaException, PosOcupadaException, CaracterNoNumericoException) as e:
                print(f"\nError: {e}")
                time.sleep(2) # Pausa para que el usuario lea el error
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                time.sleep(2)

        # 2. PAUSA Y MENSAJE ANTES DE REINICIAR
        print("\nLa siguiente partida comenzará en 5 segundos...")
        time.sleep(5)
        # Al terminar esta línea, el bucle principal (while True) vuelve a empezar

if __name__ == '__main__':
    main()