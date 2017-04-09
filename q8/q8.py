import csv, logging, math
from datetime import datetime
from Boy import Boy
from miserBoy import miserBoy
from geekBoy import geekBoy
from generousBoy import generousBoy
from Girl import Girl
from choosyGirl import choosyGirl
from desperateGirl import desperateGirl
from normalGirl import normalGirl
from Gift import Gift
from essentialGift import essentialGift
from luxuryGift import luxuryGift
from utilityGift import utilityGift
from Couple import Couple
import utilities

def loadData():   




	"""Loads random boys, girls and gifts from csv file into the program"""

	try:
		with open('randomBoys.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')

			for row in reader:
				if row[5] == 'miser':
					temp = miserBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))
				elif row[5] == 'generous':
					temp = generousBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))
				else:
					temp = geekBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))
				boysList.append(temp)
			csvfile.close()
	except:
		pass

	try:
		with open('randomGirls.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				if row[5] == 'desperate':
					temp = desperateGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4])
				elif row[5] == 'choosy':
					temp = choosyGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4])
				else:
					temp = normalGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4])
				girlsList.append(temp)
			csvfile.close()
	except:
		pass

	try:
		with open('randomGifts.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				if row[0] == 'essential':
					temp = essentialGift(int(row[1]), int(row[2]))
				elif row[0] == 'luxury':
					temp = luxuryGift(int(row[1]), int(row[2]), int(row[3]), int(row[4]))
				else:
					temp = utilityGift(int(row[1]), int(row[2]), int(row[3]), int(row[4]))
				giftsList.append(temp)

			csvfile.close()
	except:
		pass







if __name__ == '__main__':

	utilities.generateRandomItems() 
	"""call to utility function to generate random items"""
	logging.basicConfig(filename='q8Log.txt',level=logging.DEBUG)			
	boysList, girlsList, giftsList, couplesList = [], [], [], []		
	loadData() 
	"""call to the function loadData() to load data in csv files into the program."""
	#print len(giftsList)	

	for girl in girlsList:
		"""this loop assigns bf's to girls"""						
		for boy in boysList:
			if girl.canDateThisBoy(boy) and boy.canDateThisGirl(girl):
				girl.getCommitted(boy)
				boy.getCommitted(girl)
				couplesList.append(Couple(girl, boy))
				logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt

	algo = int(raw_input("Enter 1 to Select old logic for gifting and 2 for new logic for gifting-------->"))
	
	if (algo == 1):
		print "Gifting according to old logic"
		for couple in couplesList:				# the loop sets giftBasket for each couple and set happiness and compability of each 
			boy = couple.boy				# couple
			girl = couple.girl
			giftBasket = boy.setGiftBasket(giftsList, girl)
			girl.receiveGifts(giftBasket)
			logging.info("%s >>>boy %s is gifting gifts %s to girl %s" %(str(datetime.now()), boy.name, str(giftBasket), girl.name))
			boy.setHappiness()
			couple.happiness = girl.happiness + boy.happiness
			couple.compatibility = (boy.budget - girl.maintainenceBudget) + math.fabs(boy.attractiveness - girl.attractiveness) + math.fabs(boy.intelligenceLevel - girl.intelligenceLevel)
	else:
		print "Gifting according to new logic"
		for couple in couplesList:				# the loop sets giftBasket for each couple according to new gifting logic
			boy = couple.boy				    # and set happiness and compability of each 
			girl = couple.girl
			giftBasket = boy.newGifting(giftsList)
			girl.receiveGifts(giftBasket)
			logging.info("%s >>>boy %s is gifting gifts %s to girl %s" %(str(datetime.now()), boy.name, str(giftBasket), girl.name))
			boy.setHappiness()
			couple.happiness = girl.happiness + boy.happiness
			couple.compatibility = (boy.budget - girl.maintainenceBudget) + math.fabs(boy.attractiveness - girl.attractiveness) + math.fabs(boy.intelligenceLevel - girl.intelligenceLevel)
	
