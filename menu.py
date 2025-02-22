#importamos clase colorama para poder tener colores por consola
"""Esta clase llevará el control de los menus textuales del juego"""
from colorama import init, Fore, Back
from reto import Reto
import sys, tty, termios
import os
import json

class Menu():

    def __init__(self,idioma):

        self.nro_menu:  int	= 0
        self.selection: int     = 0
        self.idioma             = idioma


    def show_menu(self, nro_menu: int):
        self.selection = 0
        correcto: bool = False

        init()

        if nro_menu==0:

            while not correcto:
                try:
                   print (Fore.WHITE+" Escoge una opción:    ")
                   print (Fore.WHITE+"-----------------------")
                   print (Fore.WHITE+"| 1 . Ayuda           |")
                   print (Fore.WHITE+"| 2 . Cargar partida  |")
                   print (Fore.WHITE+"| 3 . Nueva partida   |")
                   print (Fore.WHITE+"| 99. Salir           |")
                   print (Fore.WHITE+"-----------------------")
                   print ("\n")

                   self.selection = int(input("#>>"))

                   if not (1 <= self.selection <= 3 or self.selection == 99):
                       raise ValueError("")
                   else:
                       correcto=True
                except ValueError:
                    print ("\n Opción no válida\n")


        elif nro_menu==1: # AYUDA #

            while not correcto:
                try:
                    os.system("clear")
                    print (Fore.WHITE+"-------------------------------") 
                    print (Fore.WHITE+"| Manual de usuario Heroquest |")
                    print (Fore.WHITE+"-------------------------------") 
                    print (Fore.WHITE+"| 1 . Simbología en el mapa   |")
                    print (Fore.WHITE+"| 2 . Imprimir el mapa base   |") 
                    print (Fore.WHITE+"| 3 . Volver a menú principal |") 
                    print (Fore.WHITE+"-------------------------------")
                    print ("\n")
                    self.selection = int(input("#>>"))

                    if not (1 <= self.selection <= 3 or self.selection == 99):
                       raise ValueError("")
                    else:
                       correcto=True
                except ValueError:
                    print ("\n Opción no válida\n")

        elif nro_menu==2: # CARGAR PARTIDA #
            os.system("clear")
            print (Fore.WHITE+"-----------------------------------------") 
            print(Fore.WHITE+"|         Elige uno de los retos:       |")
            print (Fore.WHITE+"-----------------------------------------") 

            retos_dir = 'saved'  # Directorio que contiene las carpetas de retos
            retos = [d for d in os.listdir(retos_dir) if os.path.isdir(os.path.join(retos_dir, d))]

            # Mostrar los retos disponibles con su título desde el archivo JSON
            for idx, reto in enumerate(retos, 1):
                datos_file = os.path.join(retos_dir, reto, f"{reto}c.json")
                try:
                    with open(datos_file, 'r') as f:
                        datos = json.load(f)
                        titulo = datos.get('titulo', 'Título no disponible')
                except (FileNotFoundError, json.JSONDecodeError):
                    titulo = 'Título no disponible'

                print(f"{Fore.WHITE}|  {idx}. {titulo} \t\t|")

            
            print (Fore.WHITE+"-----------------------------------------") 
            
            while not correcto:
                try:
                    nro_reto = int(input("\nSelecciona el número del reto: "))
                    
                    # Verificar si el número seleccionado está en el rango válido
                    if 1 <= nro_reto <= len(retos):
                        reto_seleccionado = retos[nro_reto -1] #en python los arrays inician en cero
                        correcto=True
                except (ValueError, IndexError):
                    print("Opción no válida.")
                    correcto=False

            # Cargar los archivos del reto seleccionado
            mapa_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}a.txt")
            historia_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}b.txt")
            datos_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}c.json")
            _reto.show_story()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
            _reto.show_map()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
            _reto.show_stats()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos



        elif nro_menu==3: # NUEVA PARTIDA #

            os.system("clear")

            print (Fore.WHITE+"-----------------------------------------") 
            print(Fore.WHITE+"|         Elige uno de los retos:       |")
            print (Fore.WHITE+"-----------------------------------------") 

            retos_dir = 'retos'  # Directorio que contiene las carpetas de retos
            retos = [d for d in os.listdir(retos_dir) if os.path.isdir(os.path.join(retos_dir, d))]

            # Mostrar los retos disponibles con su título desde el archivo JSON
            for idx, reto in enumerate(retos, 1):
                datos_file = os.path.join(retos_dir, reto, f"{reto}c.json")
                try:
                    with open(datos_file, 'r') as f:
                        datos = json.load(f)
                        titulo = datos.get('titulo', 'Título no disponible')
                except (FileNotFoundError, json.JSONDecodeError):
                    titulo = 'Título no disponible'

                print(f"{Fore.WHITE}|  {idx}. {titulo} \t\t|")            
                
            print (Fore.WHITE+"-----------------------------------------") 
            
            while not correcto:
                try:
                    nro_reto = int(input("\nSelecciona el número del reto: "))
                    # Verificar si el número seleccionado está en el rango válido
                    if 1 <= nro_reto <= len(retos):
                        reto_seleccionado = retos[nro_reto -1] #en python los arrays inician en cero
                        correcto=True
                except (ValueError, IndexError):
                    print("Opción no válida.")
                    correcto=False

            # Cargar los archivos del reto seleccionado
            mapa_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}a.txt")
            historia_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}b.txt")
            datos_file = os.path.join(retos_dir, reto_seleccionado, f"{reto_seleccionado}c.json")
            _reto = Reto(mapa_file, historia_file, datos_file)
            _reto.show_story()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
            _reto.show_map()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
            _reto.show_stats()
            goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
