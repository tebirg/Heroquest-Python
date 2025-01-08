from colorama import init, Fore, Back
import sys, tty, termios
import os
import json

class Help():

    def __init__(self, idioma):
        self.nro_menu: int      = 0
        self.idioma             = idioma

    def show_menu(self, nro_menu: int):
        self.selection = 0
        correcto: bool = False

        init()

        if nro_menu == 1:
            self.show_help_file()
        elif nro_menu == 2:
            self.show_map_file()




    def show_help_file(self):
        """
        Muestra el contenido del archivo simbologia.txt ubicado en la carpeta 'ayuda'.
        Se presenta de forma estructurada y legible.
        """
        help_file_path = os.path.join("ayuda", "simbologia.txt")
        
        if os.path.exists(help_file_path):
            with open(help_file_path, "r", encoding="utf-8") as file:
                # Leer el contenido del archivo
                help_content = file.read().strip().splitlines()

                print(Fore.CYAN + "\n================= Simbología del Juego =================")
                print(Fore.YELLOW + "Símbolo\t\tDescripción")
                print(Fore.CYAN + "=======================================================")

                for line in help_content:
                    parts = line.split("\t")  # Separar símbolo y descripción por tabulación
                    if len(parts) == 2:
                        symbol, description = parts
                        print(Fore.GREEN + f"{symbol}\t\t{description}")
                    else:
                        # Si no tiene la estructura esperada, lo muestra como está
                        print(Fore.RED + f"Error de formato en la línea: {line}")

                print(Fore.CYAN + "=======================================================")

        else:
            print(Fore.RED + "El archivo 'simbologia.txt' no se encuentra en la carpeta 'ayuda'.")
            
    def show_map_file(self):
        """Muestra el contenido del archivo vacio.txt ubicado en la carpeta 'ayuda' en referencia a un mapa sin nada.
        Se presenta de forma estructurada y legible, cambiando el color de los caracteres no cuadrados (■)."""
        help_file_path = os.path.join("ayuda", "vacio.txt")
    
        if os.path.exists(help_file_path):
            with open(help_file_path, "r", encoding="utf-8") as file:
                # Leer el contenido del archivo
                map_content = file.read().strip().splitlines()

                print(Fore.CYAN + "=========================================================================================================================================")
                print(Fore.CYAN + "============================================ Mapa en blanco del Juego ===================================================================")
                print(Fore.CYAN + "=========================================================================================================================================")

                # Procesar cada línea del mapa
                for line in map_content:
                    line_output = ""
                    # Elimina los números (puedes usar una expresión regular para eliminar cualquier número)
                    line_without_numbers = ''.join([char if not char.isdigit() else ' ' for char in line])
                    
                    for char in line_without_numbers:
                        if char == "■":
                            line_output += Fore.LIGHTWHITE_EX + char  # Color verde para los cuadrados
                        else:
                            line_output += Fore.RED + char  # Color amarillo para los demás caracteres
                    print(line_output)

                print(Fore.CYAN + "=========================================================================================================================================")

        else:
            print(Fore.RED + "El archivo 'vacio.txt' no se encuentra en la carpeta 'ayuda'.")


