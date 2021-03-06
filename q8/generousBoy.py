from luxuryGift import luxuryGift
from essentialGift import essentialGift
from utilityGift import utilityGift
from Boy import Boy

class generousBoy(Boy):

	def __init__(self, name, attractiveness, intelligenceLevel, budget, minAttractionReq):
		self.name = name
		self.attractiveness = attractiveness 
		"""represents attractiveness of the boy"""
		self.intelligenceLevel = intelligenceLevel
		"""represents intelligencelevel of the boy"""	
		self.budget = budget
		"""represents budget of the boy"""				
		self.minAttractionReq = minAttractionReq
		"""represents the minimum attraction level the girl need to have to date this boy"""	
		self.isCommitted = False
		"""represents status of the boy True depicts that boy is in relationship and False depicts that he is single """			
		self.gf = None
		"""this stores the instance of Girl Class who is gf of this boy"""					
		self.happiness = 0
		"""this represents happiness of the boy, initially it is 0"""				
		self.expenditure = 0
		"""reprents the amount the boy has spent on gifting"""




	def Gifting(self, giftsList, girl): 
		"""
			the method sets the giftbasket according to generous gifting logic and returns the 
			so populated giftBasket as a list
			Arguments:
				giftsList[list] (list of all the available gifts)
				girl[Girl] 
		"""
		counter = 0
		items = 0
		giftBasket = []
		for gift in sorted(giftsList, key = lambda x : x.price, reverse = True):
			if counter + gift.price <= self.budget:
				giftBasket.append(gift)
				counter += gift.price
				items += 1
		self.expenditure = counter
		return giftBasket


	


	def setGiftBasket(self, giftsList, girl):	
		"""
			sets and return the giftBasket.
				Arguments:
				giftsList[list] (list of all the available gifts)
				girl[Girl]
		"""
		return self.Gifting(giftsList, girl)
		
	def setHappiness(self): 
		"""
			sets happiness of the generous boy = happines of his gf
			***Takes no arguments
		"""
		self.happiness = self.gf.happiness
		



