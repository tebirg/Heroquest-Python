#importamos clase colorama para poder tener colores por consola
"""Esta clase llevará el control de cada uno de los retos"""
from colorama import init, Fore, Back
import sys, tty, termios
import os
import json

class Reto():

    def __init__(self, nro_reto, mapa_file, historia_file, datos_file):
	
        self.nro_reto:int = nro_reto # Número de carpeta del reto #
        self.dificultades = {
            "Baja": {"descripcion": "Ideal para principiantes", "puntos": 10},
            "Media": {"descripcion": "Requiere algo de experiencia", "puntos": 20},
            "Alta": {"descripcion": "Desafiante, para jugadores experimentados", "puntos": 30},
            "Experto": {"descripcion": "Solo para los más valientes", "puntos": 50}
        }
        
        
        self.mapa_file = mapa_file
        self.historia_file = historia_file
        self.datos_file = datos_file
        
        try:
            with open(self.datos_file, 'r') as f:
                datos = json.load(f)
                
            self.dificultad = datos.get('dificultad', 'No disponible')    
            
        except (FileNotFoundError, json.JSONDecodeError):
            # En caso de error, asignamos la dificultad a un valor predeterminado
            self.dificultad = 'No disponible'
            print(f"Error al cargar el archivo de datos para el reto {self.nro_reto}. Se asigna dificultad predeterminada.")
            
        # Opcionalmente podrías verificar que la dificultad esté en el diccionario de dificultades
        if self.dificultad not in self.dificultades:
            print(f"Dificultad '{self.dificultad}' no reconocida. Se asigna dificultad predeterminada: 'Baja'.")
            self.dificultad = "Baja"  # Asignamos un valor predeterminado en caso de dificultad inválida
        

        
    def show_map(self):
        # Mostrar el mapa
        try:
            with open(self.mapa_file, 'r') as f:
                mapa = f.read()
            print("\nMapa del reto:")
            print(mapa)
        except FileNotFoundError:
            print("No se pudo cargar el mapa.")


    def show_story(self):
        # Mostrar la historia
        try:
            with open(self.historia_file, 'r') as f:
                historia = f.read()
            print("\nHistoria del reto:")
            print(historia)
        except FileNotFoundError:
            print("No se pudo cargar la historia.")


    def show_stats(self):
        # Mostrar los datos del reto
        try:
            with open(self.datos_file, 'r') as f:
                datos = json.load(f)
            print("\nDatos del reto:")
            print(f"Título: {datos.get('titulo', 'No disponible')}")
            print(f"Dificultad: {datos.get('dificultad', 'No disponible')}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No se pudieron cargar los datos del reto.")
