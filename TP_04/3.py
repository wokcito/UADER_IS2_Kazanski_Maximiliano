class PrintPieza():
	def printPieza(self, father = None):
		pass

class Conjunto(PrintPieza):
	def __init__(self, name):
		self.name = name
		self.children = []

	def add(self, child):
		self.children.append(child)
	
	def remove(self, child_id):
		self.children.pop(child_id)

	def printPieza(self, father = None):
		if father is None:
			print(self.name)
		else:
			print(f'{father} | {self.name}')

		if len(self.children) > 0:
			for i in self.children:
				i.printPieza(self.name)

class Pieza(PrintPieza):
	def __init__(self, name):
		self.name = name
	
	def printPieza(self, father):
		print(f'{father} | {self.name}')

producto = Conjunto("Producto principal")

subconjunto1 = Conjunto("Subconjunto 1")
subconjunto2 = Conjunto("Subconjunto 2")
subconjunto3 = Conjunto("Subconjunto 3")

producto.add(subconjunto1)
producto.add(subconjunto2)
producto.add(subconjunto3)

pieza1 = Pieza("Pieza #1")
pieza2 = Pieza("Pieza #2")
pieza3 = Pieza("Pieza #3")
pieza4 = Pieza("Pieza #4")

subconjunto1.add(pieza1)
subconjunto1.add(pieza2)
subconjunto1.add(pieza3)
subconjunto1.add(pieza4)

subconjunto2.add(pieza1)
subconjunto2.add(pieza2)
subconjunto2.add(pieza3)
subconjunto2.add(pieza4)

subconjunto3.add(pieza1)
subconjunto3.add(pieza2)
subconjunto3.add(pieza3)
subconjunto3.add(pieza4)

producto.printPieza()
