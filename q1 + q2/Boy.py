class Boy():

	def __init__(self, name, attractiveness, intelligenceLevel, budget, minAttractionReq):
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

	def performBreakup(self):
		self.isCommitted = False
		self.gf = None
		self.expenditure = 0


	