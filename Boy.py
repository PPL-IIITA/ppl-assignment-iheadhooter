class Boy():

	def __init__(self, name, attractiveness, intelligenceLevel, budget, minAttractionReq, trait):
		self.name = name
		self.attractiveness = attractiveness            # Initializes attractiveness of Boy
		self.intelligenceLevel = intelligenceLevel	# Initializes the Intelligence Level of Boy
		self.budget = budget				# Initializes the Budget of Boy
		self.minAttractionReq = minAttractionReq	# Initializes Minimum Attractiveness of Girl Required to Date Him
		self.trait = trait   				# Initializes trait of Boy, trait can be either of miser, generous, geek
		self.isCommitted = False			# Initializes Relationship Status to single
		self.gf = None					# Initializes GF to None
		self.happiness = 0				# Initializes happiness to 0
		self.expenditure = 0				# Initializes expenditure to none




	def canDateThisGirl(self, girl):                                      # Return True if the Boy Can Date the Girl passed as argument
		if self.isCommitted == False and girl.isCommitted == False:   # if not then Returns False
			if girl.attractiveness >= self.minAttractionReq:      
				if girl.maintainenceBudget <= self.budget:
					return True

		return False



	def getCommitted(self, girl):	     #this Method assigns a Girl as object's gf
		self.isCommitted = True
		self.gf = girl


	def miserGifting(self, giftsList, girl):             # This Method sets and returns giftBasket as per miser logic (given in question)
		counter = 0
		items = 0
		giftBasket = []
		for gift in sorted(giftsList, key = lambda x : x.price):
			if gift.price > self.budget - counter:
				self.budget = counter + gift.price
			counter += gift.price
			giftBasket.append(gift)
			items += 1
			if counter >= girl.maintainenceBudget:
				break
		self.expenditure += counter
		return giftBasket

	
	def generousGifting(self, giftsList, girl):	     # This Method sets and returns giftBasket as per Generous logic (given in question)
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


	def geekGifting(self, giftsList, girl):  	    # This Method sets and returns giftBasket as per Geek logic (given in question)
		counter = 0
		items = 0
		giftBasket = []
		for gift in sorted(giftsList, key = lambda x : x.price):
			if gift.price > self.budget - counter:
				self.budget = counter + gift.price
			counter += gift.price
			giftBasket.append(gift)
			items += 1
			if counter >= girl.maintainenceBudget:
				break
		self.expenditure += counter
		return giftBasket


	def setGiftBasket(self, giftsList, girl):	 # This Method calls one of three methods to set giftBasket depending on trait of Boy viz
		if self.trait == 'miser':		 # miser, Generous and Geek
			return self.miserGifting(giftsList, girl)
		elif self.trait == 'generous':
			return self.generousGifting(giftsList, girl)
		else:
			return self.geekGifting(giftsList, girl)

	def setHappiness(self):				 # This Method sets happiness of the instance variable depending on the Trait and Expenditure 
		if self.trait == 'miser':		 # of Boy
			self.happiness = self.budget - self.expenditure
		elif self.trait == 'generous':
			self.happiness = self.gf.happiness
		else:
			self.happiness = self.gf.intelligenceLevel



