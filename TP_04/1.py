class Ping():
	def execute(self, ip: str):
		if ip.startswith('192.') is False:
			return print('The IP should start with "192." to use execute method')

		for i in range(10):
			print(f'ping to {ip}')
	
	def executefree(self, ip: str):
		for i in range(10):
			print(f'ping to {ip}')

class PingProxy():
	def __init__(self, ping: Ping):
		self.ping = ping

	def execute(self, ip: str):
		if ip == '192.168.0.254':
			self.ping.executefree('www.google.com')
			return
		
		self.ping.execute(ip)
	
	def executefree(self, ip: str):
		self.ping.executefree(ip)

ping = Ping()
pingProxy = PingProxy(ping)

# ping.execute()
# ping.executefree()

pingProxy.execute('192.168.0.254')
