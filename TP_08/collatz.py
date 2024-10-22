def collatz(num = None):
    if num is None:
        raise Exception('Debe enviar un número')

    if not isinstance(num, int):
        raise Exception('Debe enviar un número entero positivo')

    if not 0 < num < 2000:
        raise Exception('El número debe ser mayor a 0 y menor a 2000')

    iteraciones = 0

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1

    return iteraciones

def test():
    assert isinstance(collatz(2), int), 'Error: Debe retornar un entero'
    assert collatz(1) == 0, 'Error: Para el número 1 deben ser 0 iteraciones'
    assert collatz(2) == 1, 'Error: Para el número 2 debe ser 1 iteración'
    assert collatz(3) == 7, 'Error: Para el número 3 deben ser 7 iteraciones'
    assert collatz(1999) == 50, 'Error: Para el número 1999 deben ser 50 iteraciones'

    import pytest

    with pytest.raises(Exception, match = 'El número debe ser mayor a 0 y menor a 2000'):
        collatz(0)

    with pytest.raises(Exception, match = 'El número debe ser mayor a 0 y menor a 2000'):
        collatz(2000)

    with pytest.raises(Exception, match = 'Debe enviar un número'):
        collatz()

    with pytest.raises(Exception, match = 'Debe enviar un número entero positivo'):
        collatz(1.3)

    print('Todos los tests pasaron')

test()
