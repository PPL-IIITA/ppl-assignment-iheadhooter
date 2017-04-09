import math
from Girl import Girl
from luxuryGift import luxuryGift
from essentialGift import essentialGift
from utilityGift import utilityGift

class choosyGirl(Girl):

	def __init__(self, name, attractiveness, maintainenceBudget, intelligenceLevel, choosingCriteria): 
		self.name = name
		"""represents name of the girl"""
		self.attractiveness = attractiveness
		"""represents attractiveness of the girl"""
		self.maintainenceBudget = maintainenceBudget
		"""represents maintainence budget of the girl i.e the minimum budget the boy should have to date this particular girl"""
		self.intelligenceLevel = intelligenceLevel
		"""represents intelligence level of the girl"""
		self.choosingCriteria = choosingCriteria
		"""represents choosing criteria, ie the criteria on which girl choses her partner"""
		self.isCommitted = False
		"""represents relationship status of the girl, True Depicts that she is in a relationship and Fase depicts that she is single"""
		self.exbfs = []
		"""is a list, which stores the name of the boys the girl has dated in past or is currently dating"""
		self.bf = None
		"""stores the instance of Boy class whom the girl is dating, initially it is set to none"""

	def Receive(self, giftBasket):
		"""
			this method receives giftBasket as argument and sets the happiness
			of the girl as per choosy logic

			Arguments:
				giftBasket[list] (the list of gifts presented by her bf)
		"""						
		counter = 0								
		luxuryCounter = 0										
		for gift in giftBasket:
			if isinstance(gift, luxuryGift):
				luxuryCounter += 2 * gift.value
			counter += gift.price
		if counter > 0:
			counter = math.log(counter) + luxuryCounter
		else:
			counter = luxuryCounter
		self.happiness = counter

	def receiveGifts(self, giftBasket):
		"""
			Makes call to receiveGifts
			Arguments:
				giftBasket[list] (the list of gifts presented by her bf)
		"""						
		self.Receive(giftBasket)
		
