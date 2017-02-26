import math



class Girl():

	def __init__(self, name, attractiveness, maintainenceBudget, intelligenceLevel, choosingCriteria, trait): # initializes instance of Girl Class
		self.name = name
		self.attractiveness = attractiveness
		self.maintainenceBudget = maintainenceBudget
		self.intelligenceLevel = intelligenceLevel
		self.choosingCriteria = choosingCriteria
		self.trait = trait
		self.isCommitted = False
		self.bf = None

	def canDateThisBoy(self, boy):							# Returns True if the girl can date Boy passed as argument
		if self.isCommitted == False and boy.isCommitted == False:
			if boy.budget >= self.maintainenceBudget:
				return True
		return False

	def getCommitted(self, boy):							# sets bf to Boy passed as argument
		self.isCommitted = True
		self.bf = boy

	def choosyReceive(self, giftBasket):						# sets happiness of the girl as per choosy Logic (given In
		counter = 0								# question) and giftBasket
		luxuryCounter = 0										
		for gift in giftBasket:
			if gift.type == 'luxury':
				luxuryCounter += 2 * gift.value
			counter += gift.price
		if counter > 0:
			counter = math.log(counter) + luxuryCounter
		else:
			counter = luxuryCounter
		self.happiness = counter

	def normalReceive(self, giftBasket):						# sets happiness of the girl as per normal Logic (given In
		counter = 0								# question) and giftBasket
		valCounter = 0
		for gift in giftBasket:
			counter += gift.price
			valCounter += gift.value
		counter = counter + valCounter
		self.happiness = counter

	def desperateReceive(self, giftBasket):						# sets happiness of the girl as per desperate Logic (given In
		counter = 0 								# question) and giftBasket
		for gift in giftBasket:
			counter += gift.price
		self.happiness = math.pow(math.e, counter)

	def receiveGifts(self, giftBasket):						# calls different methods to set happiness of herself depending
		if self.trait == 'choosy':						# on her trait viz. choosy, normal, desperate
			self.choosyReceive(giftBasket)
		elif self.trait == 'normal':
			self.normalReceive(giftBasket)
		else:
			self.desperateReceive(giftBasket)
