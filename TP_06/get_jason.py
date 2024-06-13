"""
Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.
"""

import sys
import json

VERSION_COMMANDS = ["-v", "--version"]
VERSION = '1.1'
HELP_COMANDS = ["-h", "--help"]
HELP_MESSAGE = """
Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

        {path ejecutable}/get_jason.pyc {path archivo JSON}/{nombre archivo JSON}.json

ej.
        ./get_jason.pyc ./sitedata.json

El token podrá recuperarse mediante el standard output de ejecución en el formato

    {1.0}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

    ./get_jason.pyc -h

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
terminar.
"""

class SingletonMeta(type):
    """
    Singleton meta class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class GetJason(metaclass=SingletonMeta):
    """
    GetJason class para unificar todos los métodos relacionados
    """

    def open_file(self, json_file):
        """
        Abre un archivo .json
        """

        try:
            with open(json_file, 'r') as myfile:
                data = myfile.read()

            return data
        except Exception:
            print(f"No se pudo abrir el archivo {json_file}, corrobore que exista")
            sys.exit()

    def get_token(self, json_file, json_key):
        """
        Obtiene el token de un archivo .json pasándole el key como parámetro
        """

        try:
            data = self.open_file(json_file)

            obj = json.loads(data)
            return obj[json_key]
        except Exception:
            print(f"No se encontró el token perteneciente al key {json_key}")
            sys.exit()

    def get_help_message(self):
        """
        Retorna el mensaje de ayuda
        """
        return HELP_MESSAGE

    def get_version(self):
        """
        Retorna el mensaje de la función
        """
        return VERSION

if __name__ == "__main__":
    args = sys.argv

    try:
        if len(args) < 3:
            raise Exception("Considere utilizar el comando -h o --help para ver el mensaje de ayuda")

        getJason = GetJason()

        for arg in args:
            if arg in VERSION_COMMANDS:
                print(getJason.get_version())
                sys.exit()

            if arg in HELP_COMANDS:
                print(getJason.get_help_message())
                sys.exit()

        _, file, key = args
        print(getJason.get_token(file, key))

    except Exception as err:
        print(err)
