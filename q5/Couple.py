from Girl import Girl
from Boy import Boy

class Couple():
	
	def __init__(self, girl, boy):			# Creates Instance of Couple
		self.girl = girl			# Initializes girl variable to passed Girl Object
		self.boy = boy				# Initializes boy variable to passed Boy Object
		self.happiness = 0			# Initializes happiness to 0
		self.compatibility = 0			# Initializes compatibility to 0
