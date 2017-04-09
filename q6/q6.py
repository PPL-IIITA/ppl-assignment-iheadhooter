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

def loadData():   # Loads Data from CSV into Program



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







if __name__ == '__main__': # Execution Begins from Here

	utilities.generateRandomItems()						# calls utility function to generate random data
	logging.basicConfig(filename='q6Log.txt',level=logging.DEBUG)			
	boysList, girlsList, giftsList, couplesList = [], [], [], []		
	loadData()				 			#calls the function which loads data from csv file to Program
	#print len(giftsList)	

	t = int(raw_input("Enter value of t(between 0 to 20)------>"))

	print "Performing Breakups of couples whose happiness is less than %d and assigning new boyfriends to recently broked up girls" %(t)
	tempList = []
	for k in range(t):
		couplesList = couplesList + tempList

		for girl in sorted(girlsList, key = lambda x : x.attractiveness, reverse = True):# The loop assigns bf's to girls in the same order as the input
			for boy in boysList:
				if girl.canDateThisBoy(boy) and boy.canDateThisGirl(girl):
					girl.getCommitted(boy)
					boy.getCommitted(girl)
					couplesList.append(Couple(girl, boy))
					logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt

		for couple in couplesList:				# the loop sets giftBasket for each couple and set happiness and compability of each 
			boy = couple.boy				# couple
			girl = couple.girl
			giftBasket = boy.setGiftBasket(giftsList, girl)
			girl.receiveGifts(giftBasket)
			boy.setHappiness()
			couple.happiness = girl.happiness + boy.happiness
			couple.compatibility = (boy.budget - girl.maintainenceBudget) + math.fabs(boy.attractiveness - girl.attractiveness) + math.fabs(boy.intelligenceLevel - girl.intelligenceLevel)

		#Performing Breakup of Couples whose happiness is less than t and assigning new bf's to the girl
		
		tempList = []
		for couple in couplesList:
			if couple.happiness < t:
				girl = couple.girl
				boy = couple.boy
				couplesList.remove(couple)
				boy.performBreakup()
				girl.performBreakup()
				logging.info("%s >>>girl %s and Boy %s just broked up" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt
				for temp in boysList:
					if temp.canDateThisGirl(girl) and girl.canDateThisBoy(boy):
						temp.getCommitted(girl)
						girl.getCommitted(temp)
						tempList.append(Couple(girl, temp))
						logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, temp.name)) # Logs TimeStamp and Committments into q1Log.txt
						break
