from Gift import Gift

class luxuryGift(Gift):

	def __init__(self, price, value, luxuryRating, difficultyToObtain): 
		self.price = price
		"""represents price of the gift"""
		
		self.value = value
		"""represents value of the gift"""

		self.luxuryRating = luxuryRating
		"""represents luxuryry Rating of the gift"""
		
		self.difficultyToObtain = difficultyToObtain
		"""represents the difficulty caused to obtain the gift"""