# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import sys

HELP_COMAND = "-h"

if HELP_COMAND in sys.argv:
    print("""
        Este programa permite extraer la clave de acceso API para utilizar los servicios del 
        Banco XXX.

        El programa operará como un microservicio invocado mediante:

                {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

        ej.
                ./getJason.pyc ./sitedata.json

        El token podrá recuperarse mediante el standard output de ejecución en el formato

            {1.0}XXXX-XXXX-XXXX-XXXX

        Para obtener un mensaje de ayuda detallado ejecutar

            ./getJason.pyc -h

        Excepciones

        Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
        terminar.
    """)
    sys.exit()

import json

jsonfile = sys.argv[1]
jsonkey = sys.argv[2]

with open(jsonfile, 'r') as myfile:
	data = myfile.read()

obj = json.loads(data)
print(obj[jsonkey])

# okay decompiling ./getJason.pyc
