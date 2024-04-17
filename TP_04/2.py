class Lamina:
    def __init__(self, espesor, ancho):
        self.espesor = espesor
        self.ancho = ancho

    def cortar(self, longitud):
        print(f'La lámina se corta cada {longitud} metros, y tiene {self.ancho} metros de ancho y un espesor de {self.espesor} pulgadas.')

class Laminador:
    def __init__(self, lamina: Lamina): pass
    def cortar_lamina(self, ancho, espesor): pass

class LaminadorCorto(Laminador):
    def __init__(self, lamina: Lamina):
        self.lamina = lamina

    def cortar_lamina(self):
        self.lamina.cortar(5)

class LaminadorLargo(Laminador):
    def __init__(self, lamina: Lamina):
        self.lamina = lamina

    def cortar_lamina(self):
        self.lamina.cortar(10)

lamina = Lamina(0.5, 1.5)

laminador_corto = LaminadorCorto(lamina)
laminador_largo = LaminadorLargo(lamina)

laminador_corto.cortar_lamina()
laminador_largo.cortar_lamina()
