## 1.

## 2.

### a.

### b.

#### Paso 1
Descargué todos los archivo del RRR_TP6.tar.gz que contiene los binarios, documentación y el .json con información.

#### Paso 2
Ejecuté los siguientes comandos presentes en la documentación obtenida.

```sh
python3 ./getJason.pyc ./sitedata.json

python3 ./getJason.pyc -h
```

Generaron este error.

```sh
RuntimeError: Bad magic number in .pyc file
```

#### Paso 3
Utilizando `uncompyle6` decompilo el archivo `getJason.pyc` y obtengo el siguiente resultado, guardándolo en el archivo `getJason.py`.

```py
# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey])

# okay decompiling ./getJason.pyc
```

Ejecuté los siguientes comandos:
```sh
python3 ./getJason.py

python3 ./getJason.py -h

python3 ./getJason.py ./sitedata.json
```

En todos los casos se genera el siguiente error:
```sh
print str(obj[jsonkey])
    ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

#### Paso 4
#### Paso 5
#### Paso 6

### d.
Utilizando `uncompyle6` decompilo el archivo `getJason.pyc` y obtengo el siguiente resultado, guardándolo en el archivo `getJason.py`.

```py
# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey])

# okay decompiling ./getJason.pyc
```

### f.
Las diferencias que pude encontrar fueron:
- El archivo contiene un error al ejecutarlo.
- El comando `-h` no funciona. No está contemplado en el archivo decompilado.

### g.
Al modificar el archivo getJason.py para que actúe como indica la documentación, me queda lo siguiente:

```py
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
```

### h.
Se validó el archivo getJason.py con la versión de python `3.10.12` y funciona correctamente.

### i.
Archivo `getJason.py` sin comentarios del decompilador.

```py
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
```

### j.
Compilé el getJason.py con el siguiente comando y generó el archivo `getJason.310.pyc`.

```sh
python3 -m compileall getJason.py
```

### k.
Utilizando el argumento `-h` y `./sitedata.json token1` se comprobó que funciona correctamente el archivo compilado.

## 3.

