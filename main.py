#Inicio del juego
#Aqui se encontrarán las funciones de apertura de partidas, guardado de partidas y todo lo referente a cosas genéricas del juego
"""Esta es la clase inicial. Aqui salen los menús de elección de usuario e historia a jugar. """
from colorama import init, Fore, Back
from menu import Menu
from playsound import playsound
import os

playsound('./sonidos/melodia.mp3',block=False)

os.system("clear")
print ("\n")
print ("\n")
print (Fore.YELLOW+"#>The tErMinAl rOl gaMe") 
#print (Fore.GREEN+ "   ▄█    █▄       ▄████████    ▄████████  ▄██████▄  ████████▄   ███    █▄     ▄████████    ▄████████     ███    ") 
#print (Fore.GREEN+ "  ███    ███     ███    ███   ███    ███ ███    ███ ███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄") 
#print (Fore.GREEN+ "  ███    ███     ███    █▀    ███    ███ ███    ███ ███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██") 
#print (Fore.GREEN+ " ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███ ███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀") 
#print (Fore.YELLOW+"▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███    ")  
#print (Fore.YELLOW+"  ███    ███     ███    █▄  ▀███████████ ███    ███ ███    ███  ███    ███   ███    █▄           ███     ███    ")  
#print (Fore.YELLOW+"  ███    ███     ███    ███   ███    ███ ███    ███ ███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███    ")  
#print (Fore.YELLOW+"  ███    █▀      ██████████   ███    ███  ▀██████▀   ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀  ")  
#print (Fore.YELLOW+"                              ███    ███                                                                        ")
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print (Fore.RED+"|"+Fore.YELLOW+"    █    █▄    ▄█████▄  ████████ ██████▄ ██████▄   ▄   ▄   ▄██████   ████          "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    ██    ██   ██   ██   ██ ██   ██ ██   ██  ██   ██  ██  ███  ██ ██ ▀██████▄ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    ██    ██   █▀   ██   ██ ██   ██ ██   ██  ██   ██  ██  █▀   ██ █▀   ▀██▀██ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "  ▄██▄▄▄▄██▄▄ ▄██▄▄▄    ▄██▄▄▄█▀ ██   ██ ██   ██  ██   ██  ██▄▄     ██       ██  ▀ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ " ▀▀██▀▀▀▀██▀  ▀██▀▀▀    ▀██▀▀▀▀▀ ██   ██ ██   ██  ██   ██ ▀██▀▀    ▀█████    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "   ██    ██    ██   █▄ ▀████████ ██   ██ ██ █ ██  ██   ██  ██  █▄      ██    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "   ██    ██    ██   ██   ██   ██ ██   ██ ██  ███  ██   ██  ██  ███ ▄█  ██    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    █▀    ███████   ██   ██ ▀████▀  ▀██████ ▄███████▀ ███████▄██████▀ ▄████▀  "+Fore.RED+"| ")
#print (Fore.YELLOW+"|                                                                                   "+Fore.RED+"| ")
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print (Fore.LIGHTRED_EX+"                              ©Esteban Rodriguez                                    "+Fore.RED+"| ")
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print ("\n")

init()

_menu = Menu()
_menu.show_menu(1)

if _menu.selection==1:
    _menu.show_menu(2)
    