#Inicio del juego
#Aqui se encontrarán las funciones de apertura de partidas, guardado de partidas y todo lo referente a cosas genéricas del juego
"""Esta es la clase inicial. Aqui salen los menús de elección de usuario e historia a jugar. """
from colorama import init, Fore, Back
from menu import Menu
from help import Help
from system_instance import system_instance, INICIAL, FINAL # Se crea sobre una clase estática
import pygame
import os,sys

# Ajustar el tamaño del terminal
sys.stdout.write(f"\033[8;{50};{140}t")
sys.stdout.flush()


#playsound('./sonidos/melodia.mp3',block=False)
# Cargar el sonido (asegúrate de tener un archivo .wav o .mp3 en el directorio)
# Inicializar el módulo de audio de pygame
pygame.mixer.init()
pygame.mixer.music.load('./sonidos/melodia.mp3')
# Reproducir el sonido de forma infinita
pygame.mixer.music.play(loops=-1)  # loops=-1 hace que se repita indefinidamente
# Reproducir el sonido
pygame.mixer.music.play()

system_instance.command_execute('clear')
system_instance.dibuja(INICIAL)

wexit: bool = False

_menu = Menu("sp")                                                       #Por el momento en castellano#

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
       
       if _menu.selection in(1,2):
           goOn = str(input(""))                                        #Se queda a la espera para que lea la ayuda, en el intro limpiamos pantalla. Para opcion volver a menu inicial no lo hacemos
       system_instance.command_execute('clear')
       
        
    elif _menu.selection==2:
        _menu.show_menu(2)
    elif _menu.selection==3:
        _menu.show_menu(3)
        
        
        
    elif _menu.selection==99:
        system_instance.dibuja(FINAL)
        wexit=True
    
    if not wexit:    
        system_instance.command_execute('clear')
