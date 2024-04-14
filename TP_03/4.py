class FacturaBuilder():
	def setAmount(self, amount: float):
		pass
	
	def setIVACondition(self):
		pass

class Factura():
	def __str__(self):
		return f'{self.amount} {self.condition}'

	def setAmount(self, amount: float):
		self.amount = amount
	
	def getAmount(self):
		return self.amount

	def setIVACondition(self, condition: str):
		self.condition = condition
	
	def getIVACondition(self):
		return self.condition

class Responsable(FacturaBuilder):
	def __init__(self):
		self.factura = Factura()
	
	def setAmount(self, amount: float):
		self.factura.setAmount(amount)
	
	def setIVACondition(self, condition: str):
		self.factura.setIVACondition(condition)
	
	def getResult(self):
		return self.factura

class NoInscripto(FacturaBuilder):
	def __init__(self):
		self.factura = Factura()
	
	def setAmount(self, amount: float):
		self.factura.setAmount(amount)
	
	def setIVACondition(self, condition: str):
		self.factura.setIVACondition(condition)
	
	def getResult(self):
		return self.factura

class Exento(FacturaBuilder):
	def __init__(self):
		self.factura = Factura()
	
	def setAmount(self, amount: float):
		self.factura.setAmount(amount)
	
	def setIVACondition(self, condition: str):
		self.factura.setIVACondition(condition)
	
	def getResult(self):
		return self.factura

responsable = Responsable()
responsable.setAmount(123)
responsable.setIVACondition('Responsable')
print(responsable.getResult())

noInscripto = NoInscripto()
noInscripto.setAmount(1234)
noInscripto.setIVACondition('No inscripto')
print(noInscripto.getResult())

exento = Exento()
exento.setAmount(12345)
exento.setIVACondition('Exento')
print(exento.getResult())
