class Handler():
	def set_next(self): pass
	def handle(self):pass

class PrimosHandler(Handler):
	next: int = None

	def set_next(self, next: Handler):
		self.next = next

	def handle(self, number: int):
		is_prime = self.is_prime(number)

		if is_prime:
			print(f'Primo: {number}')

		if self.next is not None and is_prime is False:
			self.next.handle(number)

	def is_prime(self, number):
		if number <= 1:
			return False
		for i in range(2, int(number**0.5) + 1):
			if number % i == 0:
				return False
		return True

class ParesHandler(Handler):
	next: int = None

	def set_next(self, next: Handler):
		self.next = next

	def handle(self, number: int):
		is_even = self.is_even(number)

		if is_even:
			print(f'Par: {number}')

		if self.next is not None and is_even is False:
			self.next.handle(number)

	def is_even(self, number):
		if number % 2 == 0:
			return True
		else:
			return False

class NoConsumidoHandler(Handler):
	next: int = None

	def set_next(self, next: Handler):
		self.next = next

	def handle(self, number: int):
		print(f'No consumido: {number}')

		if self.next is not None:
			self.next.handle(number)

primos = PrimosHandler()
pares = ParesHandler()
no_consumido = NoConsumidoHandler()

primos.set_next(pares)
pares.set_next(no_consumido)

for n in range(1, 101):
	primos.handle(n)
