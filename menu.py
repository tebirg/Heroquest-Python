#importamos clase colorama para poder tener colores por consola
"""Esta clase llevará el control de los menus textuales del juego"""
from colorama import init, Fore, Back
import sys, tty, termios
import os

class Menu():

    def __init__(self):
	
        self.nro_menu:  int	= 0
        self.selection: int = 0
  
  
  
  
    def show_menu(self, nro_menu: int):
        self.selection = 0
        correcto: bool = False
        
        init()
        
        if nro_menu==0:    
            
            while not correcto:
                try:
                   print (Fore.WHITE+" Escoge una opción:    ")
                   print (Fore.WHITE+"-----------------------")
                   print (Fore.WHITE+" 1 . Ayuda              ")
                   print (Fore.WHITE+" 2 . Cargar partida     ")
                   print (Fore.WHITE+" 3 . Nueva partida      ")
                   print (Fore.WHITE+" 99. Salir              ")
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
                    print (Fore.WHITE+"Manual de usuario Heroquest")
                    print (Fore.WHITE+"---------------------------") 
                    print (Fore.WHITE+" 1 . Simbología en el mapa ")
                    print (Fore.WHITE+" 2 . Imprimir el mapa base ") 
                    print (Fore.WHITE+" 3 . Volver a menú principal") 
                    print ("\n")
                    self.selection = int(input("#>>"))
                   
                    if not (1 <= self.selection <= 3 or self.selection == 99):
                       raise ValueError("")
                    else:
                       correcto=True
                except ValueError:
                    print ("\n Opción no válida\n")                     
            
        elif nro_menu==2: # CARGAR NUEVA PARTIDA #
            os.system("clear")
            
        elif nro_menu==3: # SELECCION DE RETO #
            os.system("clear")
            print ("\n")
            print (" Elige uno de los retos  ")
            print ("_________________________")
            print ("  1 . La furia de Ragnar ")
            print ("\n")
            
        elif nro_menu==4:
            os.system("clear")
