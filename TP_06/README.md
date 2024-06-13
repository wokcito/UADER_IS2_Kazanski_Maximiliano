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

### c.
Agregué el paquete uncompyle6 al archivo requirements.txt

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

```py
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
```

![alt text](image.png)

## 4

Al finalizar el punto cuatro el archivo queda así

```py
# get_jason.py

"""
Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.
"""

import sys
import json

VERSION_COMMANDS = ["-v", "--version"]
VERSION = '1.2'
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

class PaymentHandler:
    """
    Clase para manejar los pagos utilizando el patrón chain of responsability
    """
    def __init__(self, token, balance):
        self.token = token
        self.balance = balance
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def process_payment(self, order_number, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Pedido {order_number} pagado usando {self.token} por un monto de {amount}.")
            return {
                "order_number": order_number,
                "token": self.token,
                "amount": amount
            }
        elif self.next_handler:
            return self.next_handler.process_payment(order_number, amount)
        else:
            print(f"Pedido {order_number} no se pudo procesar por falta de saldo.")
            return None        

class PaymentIterator:
    """
    Clase iteradora para la lista de pagos
    """
    def __init__(self, payments):
        self._payments = payments
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._payments):
            result = self._payments[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    args = sys.argv

    try:
        if len(args) < 2:
            raise Exception("Considere utilizar el comando -h o --help para ver el mensaje de ayuda")

        getJason = GetJason()

        for arg in args:
            if arg in VERSION_COMMANDS:
                print(getJason.get_version())
                sys.exit()

            if arg in HELP_COMANDS:
                print(getJason.get_help_message())
                sys.exit()

        _, file = args


        # Crear los manejadores de pago
        token1_handler = PaymentHandler("token1", 1000)
        token2_handler = PaymentHandler("token2", 2000)

        # Configurar la cadena de responsabilidad
        token1_handler.set_next(token2_handler)

        # Lista para almacenar los pagos realizados
        payments = []

        def make_payment(order_number, amount):
            """
            Realiza un pago
            """
            result = token1_handler.process_payment(order_number, amount)
            if result:
                payments.append(result)

        def list_payments():
            """
            Lista todos los pagos realizados utilizando un iterador
            """
            payment_iterator = PaymentIterator(payments)
            for payment in payment_iterator:
                print(payment)

        # Realizar pedidos de pago como ejemplos
        make_payment(1, 500)
        make_payment(2, 500)
        make_payment(3, 500)
        make_payment(4, 500)
        make_payment(5, 500)

        # Listar pagos realizados
        list_payments()

    except Exception as err:
        print(err)
```
