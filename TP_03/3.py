class Food():
	def __init__(self, name: str, ):
		self.name = name

class Delivery():
	def delivery(self, food):
		pass

class DeliveryFactory():
	def createDelivery(self) -> Delivery:
		pass
	
	def operation():
		pass

class Mostrador(Delivery):
	def delivery(self, food):
		print('Entregado en mostrador: ' + food)

class Cliente(Delivery):
	def delivery(self, food):
		print('Retirado por el cliente: ' + food)

class Domicilio(Delivery):
	def delivery(self, food):
		print('Enviado a domicilio: ' + food)

class CreateMostrador(DeliveryFactory):
	def __init__(self, food: Food):
		self.food = food.name
	
	def createDelivery(self):
		return Mostrador()
	
	def operation(self):
		self.createDelivery().delivery(self.food)

class CreateCliente(DeliveryFactory):
	def __init__(self, food: Food):
		self.food = food.name
	
	def createDelivery(self):
		return Cliente()
	
	def operation(self):
		self.createDelivery().delivery(self.food)

class CreateDomicilio(DeliveryFactory):
	def __init__(self, food: Food):
		self.food = food.name
	
	def createDelivery(self):
		return Domicilio()
	
	def operation(self):
		self.createDelivery().delivery(self.food)

hamburguesa = Food('Hamburguesa')

mostrador = CreateMostrador(hamburguesa)
mostrador.operation()

cliente = CreateCliente(hamburguesa)
cliente.operation()

domicilio = CreateDomicilio(hamburguesa)
domicilio.operation()
