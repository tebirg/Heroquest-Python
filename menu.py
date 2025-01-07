#importamos clase colorama para poder tener colores por consola
"""Esta clase llevará el control de los menus textuales del juego"""
from colorama import init, Fore, Back
import sys, tty, termios
import os

class Menu():

    def __init__(self):
	
        self.nro_menu 		= 0
        self.selection      = 0
  
  
  
  
    def show_menu(self, nro_menu: int) -> int:
        selection: int = 0
        
        init()
        
        if nro_menu==0:    
            
            while True:
                try:
                   os.system("clear")
                   print (Fore.WHITE+" Escoge una opción:    ")
                   print (Fore.WHITE+"-----------------------")
                   print (Fore.WHITE+" 1 . Ayuda              ")
                   print (Fore.WHITE+" 2 . Cargar partida     ")
                   print (Fore.WHITE+" 3 . Nueva partida      ")
                   print (Fore.WHITE+" 99. Salir              ")
                   print ("\n")
            
                   selection = int(input("#>>"))
                   
                   if (selection<1 or selection>3 or selection!=99):
                       raise ValueError("")
                except ValueError:
                    print ("\n Opción no válida\n")                           
            
        
        elif nro_menu==1:
            os.system("clear")
            print (Fore.WHITE+"Manual de usuario Heroquest")
            print (Fore.WHITE+"---------------------------") 
            print (Fore.WHITE+" 1 . Simbología en el mapa ")
            print (Fore.WHITE+" 2 . Imprimir el mapa base ") 
            print (Fore.WHITE+" 3 . Volver a menú principal") 
            
        elif nro_menu==2:
            os.system("clear")
            
        elif nro_menu==3:
            os.system("clear")
            print ("\n")
            print (" Elige uno de los retos  ")
            print ("_________________________")
            print ("  1 . La furia de Ragnar ")
            print ("\n")
            
        elif nro_menu==4:
            os.system("clear")
        
        
        return(selection)
