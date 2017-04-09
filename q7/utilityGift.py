from Gift import Gift

class utilityGift(Gift):

	def __init__(self, price, value, utilityValue, utilityClass):   
		self.price = price
		"""represents the price of the gift"""
		self.value = value				
		"""represents the value of the gift"""
		self.utilityValue = utilityValue
		"""represents the utility value of the gift"""
		self.utilityClass = utilityClass
		"""represetns the utility class of the gift"""
