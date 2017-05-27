net_percentage = {"maker" : 1 - 0.16 / 100,
				"taker" : 1 - 0.26 / 100}

class Wallet:
	"""Basic Wallet"""
	def __init__(self, ETH, EUR):
		self.ETH = ETH
		self.EUR = EUR

	# Assumed that the amount is given in ETH
	def convert(self, amount, price, direction, maker_taker):
		net_amount = amount * net_percentage[maker_taker]

		if direction == "ETH_to_EUR":
			if (self.ETH < amount):
				return False
			self.ETH -= amount
			self.EUR += net_amount * price

		elif direction == "EUR_to_ETH":
			if (self.EUR < amount * price):
				return False
			self.ETH += net_amount
			self.EUR -= amount * price

		return True

	def getETH(self):
		return self.ETH

	def getEUR(self):
		return self.EUR
