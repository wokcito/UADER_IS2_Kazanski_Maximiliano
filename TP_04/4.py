class Number():
	def __init__(self, number: float):
		self.number = number

	def print(self):
		print(self.number)

	def get_base_number(self):
		return self.number

class NumberDecorator(Number):
	def __init__(self, base_number: Number): pass
	def print(self): pass
	def get_base_number(self): pass

class Sum2Decorator():
	def __init__(self, base_number: Number):
		self.number = base_number.get_base_number() + 2

	def print(self):
		print(self.number)

	def get_base_number(self):
		return self.number

class Mul2Decorator():
	def __init__(self, base_number: Number):
		self.number = base_number.get_base_number() * 2

	def print(self):
		print(self.number)

	def get_base_number(self):
		return self.number

class Div3Decorator():
	def __init__(self, base_number: Number):
		self.number = base_number.get_base_number() / 3

	def print(self):
		print(self.number)

	def get_base_number(self):
		return self.number

base_number = Number(2)

sum_2 = Sum2Decorator(base_number)
sum_2.print()

mul_2 = Mul2Decorator(sum_2)
mul_2.print()

div_3 = Div3Decorator(mul_2)
div_3.print()
