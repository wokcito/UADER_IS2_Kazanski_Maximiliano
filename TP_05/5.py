class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content

class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content

class FileWriterCaretaker:
	snapshot_list = []

	def save(self, writer):
		if len(self.snapshot_list) == 4:
			self.snapshot_list.pop()

		self.snapshot_list.insert(0, writer.save())

	def undo(self, writer, position = 0):
		writer.undo(self.snapshot_list[position])

caretaker = FileWriterCaretaker()

writer = FileWriterUtility("GFG.txt")

writer.write("Clase de IS2 en UADER\n")
caretaker.save(writer)

writer.write("Material adicional de la clase de patrones\n")
caretaker.save(writer)

writer.write("Material adicional de la clase de patrones II\n")
caretaker.save(writer)

writer.write("Material adicional de la clase de patrones III\n")
caretaker.save(writer)

writer.write("Material adicional de la clase de patrones IIII\n")
caretaker.save(writer)

writer.write("Material adicional de la clase de patrones IIIII\n")

print(writer.content)

print("Se ejecuta el undo")
caretaker.undo(writer, 2)

print(writer.content)
