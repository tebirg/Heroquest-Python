#Inicio del juego
#Aqui se encontrarán las funciones de apertura de partidas, guardado de partidas y todo lo referente a cosas genéricas del juego
"""Esta es la clase inicial. Aqui salen los menús de elección de usuario e historia a jugar. """
from colorama import init, Fore, Back
from menu import Menu
from help import Help
from system_instance import system_instance # Se crea sobre una clase estática
import pygame
import os

#playsound('./sonidos/melodia.mp3',block=False)
# Cargar el sonido (asegúrate de tener un archivo .wav o .mp3 en el directorio)
# Inicializar el módulo de audio de pygame
pygame.mixer.init()
pygame.mixer.music.load('./sonidos/melodia.mp3')
# Reproducir el sonido de forma infinita
pygame.mixer.music.play(loops=-1)  # loops=-1 hace que se repita indefinidamente
# Reproducir el sonido
pygame.mixer.music.play()


print ("\n")
print ("\n")
print (Fore.YELLOW+"#>The tErMinAl rOl gaMe") 
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print (Fore.RED+"|"+Fore.YELLOW+"    █    █▄    ▄█████▄  ████████ ██████▄ ██████▄   ▄   ▄   ▄██████   ████          "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    ██    ██   ██   ██   ██ ██   ██ ██   ██  ██   ██  ██  ███  ██ ██ ▀██████▄ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    ██    ██   █▀   ██   ██ ██   ██ ██   ██  ██   ██  ██  █▀   ██ █▀   ▀██▀██ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "  ▄██▄▄▄▄██▄▄ ▄██▄▄▄    ▄██▄▄▄█▀ ██   ██ ██   ██  ██   ██  ██▄▄     ██       ██  ▀ "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ " ▀▀██▀▀▀▀██▀  ▀██▀▀▀    ▀██▀▀▀▀▀ ██   ██ ██   ██  ██   ██ ▀██▀▀    ▀█████    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "   ██    ██    ██   █▄ ▀████████ ██   ██ ██ █ ██  ██   ██  ██  █▄      ██    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.GREEN+ "   ██    ██    ██   ██   ██   ██ ██   ██ ██  ███  ██   ██  ██  ███ ▄█  ██    ██    "+Fore.RED+"| ")
print (Fore.RED+"|"+Fore.YELLOW+"   ██    █▀    ███████   ██   ██ ▀████▀  ▀██████ ▄████1███▀ ███████▄██████▀ ▄████▀  "+Fore.RED+"| ")
#print (Fore.YELLOW+"|                                                                                   "+Fore.RED+"| ")
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print (Fore.LIGHTRED_EX+"                              ©Esteban Rodriguez                                    "+Fore.RED+"| ")
print (Fore.RED+"-------------------------------------------------------------------------------------    ")
print ("\n")

init()

wexit: bool = False

_menu = Menu("sp")                                                     #Por el momento en castellano#

while not wexit:
    
    _menu.show_menu(0)
    system_instance.command_execute('clear')
    if _menu.selection==1:
    
       _menu.show_menu(1)
       _help = Help("sp")
    
       if _menu.selection==1:                                            #Simbología
            _help.show_menu(1)
       elif _menu.selection==2:                                          #Mapa en blanco
            _help.show_menu(2)
        
    elif _menu.selection==2:
        _menu.show_menu(2)
    elif _menu.selection==3:
        _menu.show_menu(3)
    elif _menu.selection==99:
        print (Fore.YELLOW+ "\n# NoS VemoS poR oTRas TierrAs GeRreRO #\n") #Usar menu cuando sepamos el nro final de menus#
        wexit=True
