
class Girl():

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

	def canDateThisBoy(self, boy):
		"""
			Checks whether the girl can date the Boy instance passed as an argument
			Returns True if boy is single and has budget greater than or
			equal to maintainence budget of the girl.

			Arguments:
				 boy(Boy)
		"""							
		if self.isCommitted == False and boy.isCommitted == False:
			if boy.budget >= self.maintainenceBudget:
				return True
		return False

	def getCommitted(self, boy):
		"""
			this method assigns the boy to this girl. sets isCommited instance variable to True and sets bf to the 
			Boy Object passed as argument

			Arguments:
				boy(Boy)
		"""							
		self.isCommitted = True
		self.bf = boy 										
		self.exbfs.append(boy.name)   

	def performBreakup(self):
		"""
			Performs Breakup of the girl with her boyfriend
			unsets the isCommitted variable to False,
			sets gf to none

			***Takes no arguments
		"""								
		self.isCommitted = False			
		self.bf = None										
