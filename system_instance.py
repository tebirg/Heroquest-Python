# system_instance.py
from system import System

# Crear una instancia global de System (singleton)
system_instance = System()
system_instance.informar_SO()  # Esto solo se hace una vez para determinar el SO
