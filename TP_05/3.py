from typing import List

class Subject():
	_state: int = None
	_observers: List = []

	def attach(self, observer):
		self._observers.append(observer)
	
	def detach(self, observer):
		self._observers.remove(observer)

	def notify(self):
		for observer in self._observers:
			observer.update(self)

	def do_something(self):
		list_of_ids = [1,2,3,4,5,6,7,8]
		
		for id in list_of_ids:
			self._state = id
			self.notify()

def is_same_id(id, some_number):
	if id == some_number:
		return True
	else:
		return False

class ObserverA():
	_id: int = 1
	
	def update(self, subject: Subject):
		emited_id = subject._state

		if is_same_id(self._id, emited_id):
			print(f"ObserverA: {emited_id} is my id")

class ObserverB():
	_id: int = 8
	
	def update(self, subject: Subject):
		emited_id = subject._state

		if is_same_id(self._id, emited_id):
			print(f"ObserverB: {emited_id} is my id")

class ObserverC():
	_id: int = 6
	
	def update(self, subject: Subject):
		emited_id = subject._state

		if is_same_id(self._id, emited_id):
			print(f"ObserverC: {emited_id} is my id")

class ObserverD():
	_id: int = 4
	
	def update(self, subject: Subject):
		emited_id = subject._state

		if is_same_id(self._id, emited_id):
			print(f"ObserverD: {emited_id} is my id")

subject = Subject()

observer_a = ObserverA()
subject.attach(observer_a)

observer_b = ObserverB()
subject.attach(observer_b)

observer_c = ObserverC()
subject.attach(observer_c)

observer_d = ObserverD()
subject.attach(observer_d)

subject.do_something()
