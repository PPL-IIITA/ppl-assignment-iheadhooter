from luxuryGift import luxuryGift
from essentialGift import essentialGift
from utilityGift import utilityGift

class Boy():

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



	def canDateThisGirl(self, girl):                                      
		"""
			Checks whether the boy can date the Girl instance passed as an argument
			Returns True if Girl is single and has maintainence budget less than or
			equal to budget of the boy.

			Arguments:
				 girl(Girl)
		"""
		if self.isCommitted == False and girl.isCommitted == False:   
			if girl.attractiveness >= self.minAttractionReq:      
				if girl.maintainenceBudget <= self.budget:
					return True

		return False


	
	def getCommitted(self, girl):
		"""
			this method assigns the girl to a boy. sets isCommited instance variable to True and sets gf to the 
			Girl Object passed as argument

			Arguments:
				girl(Girl)
		"""
		self.isCommitted = True	
		self.gf = girl   				

	
	def performBreakup(self):			
		"""
			Performs Breakup of the boy with is girlfriend
			unsets the isCommitted variable to False,
			sets gf to none

			***Takes no arguments
		"""
		self.isCommitted = False
		self.gf = None    				
		self.expenditure = 0			

	def newGifting(self, giftsList):     
		"""
			New Gifting Logic according to which the gifting basket contains atleast one gift of each type
			even if their cost exceeds the budget of the boy.

			Arguments:
				giftsList[list] (list of available gifts)
		"""
		essential, utility, luxury = [], [], [] 
		for gift in giftsList:
			if isinstance(gift, luxuryGift):
				luxury.append(gift)
			elif isinstance(gift, utilityGift):
				utility.append(gift)
			elif isinstance(gift, essentialGift):
				essential.append(gift)

		giftBasket = []
		counter = 0
		items = 0

		for gift in sorted(essential, key = lambda x : x.price, reverse = True):
			giftBasket.append(gift)
			counter += gift.price
			break

		for gift in sorted(luxury, key = lambda x : x.price, reverse = True):
			giftBasket.append(gift)
			counter += gift.price
			break

		for gift in sorted(utility, key = lambda x : x.price, reverse = True):
			giftBasket.append(gift)
			counter += gift.price
			break

		for gift in sorted(giftsList, key = lambda x : x.price, reverse = True):
			if gift not in giftBasket:
				if counter + gift.price <= self.budget:
					giftBasket.append(gift)
					counter += gift.price
					items += 1

		self.expenditure = counter
		return giftBasket


	