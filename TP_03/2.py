class Tax():
	def calculate(self, amount: float):
		pass

class CalculateTax():
	def __init__(self, amount: float, tax: Tax) -> None:
		self.amount = amount
		self.tax = tax

	def calculate(self) -> float:
		return self.tax.calculate(self.amount)

class IVA(Tax):
	_percentage = 0.21

	def calculate(self, amount: float):
		return amount + amount * self._percentage

class IIBB(Tax):
	_percentage = 0.05

	def calculate(self, amount: float):
		return amount + amount * self._percentage

class ContribucionMunicipal(Tax):
	_percentage = 0.012

	def calculate(self, amount: float):
		return amount + amount * self._percentage

amount = 100

taxIVA = IVA()
taxIIBB = IIBB()
taxContribucionMunicipal = ContribucionMunicipal()

contextIVA = CalculateTax(amount, taxIVA)
contextIIBB = CalculateTax(amount, taxIIBB)
contextContribucionMunicipal = CalculateTax(amount, taxContribucionMunicipal)

print(contextIVA.calculate()) # 121
print(contextIIBB.calculate()) # 105
print(contextContribucionMunicipal.calculate()) # 101.2
