class Gift():

	def __init__(self, type, price, value, Par3, Par4):      # Creates Gift Instance
		
		self.type = type  				 # Sets type to either of Specified type viz. essential, luxury, utility
		self.price = price				 # Sets Specified Price to price variable
		self.value = value				 # Sets Specified Value to value variable
		self.Par3 = Par3				 # should be ignored if type == essential, consider Par3 as difficulty of obtain if  
								 # luxury and utilityValue if type == utility
		self.Par4 = Par4				 # should be ignored if type == essential

