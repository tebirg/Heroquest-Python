import subprocess
import os

class System:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(System, cls).__new__(cls)
            cls._instance.so = ""
        return cls._instance

    def informar_SO(self):
        """Determina el sistema operativo en el que se está ejecutando el código."""
        if os.name == 'nt':       # Windows
            self.so = 'windows'
        elif os.name == 'posix':  # Linux/macOS
            self.so = 'linux'

    def translate(self, comando):
        """Convierte comandos de Linux a Windows si es necesario."""
        # Por defecto los comandos llegarán en formato Linux
        if self.so == "windows":
            if comando == "clear":
                comando = "cls"
        return comando

    def command_execute(self, comando):
        """Ejecuta un comando usando el sistema operativo correcto."""
        comando = self.translate(comando)  # Traducir el comando si es necesario
        subprocess.run(comando, shell=True)