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
	logging.basicConfig(filename='q4Log.txt',level=logging.DEBUG)			
	boysList, girlsList, giftsList, couplesList = [], [], [], []		
	loadData()				 			#calls the function which loads data from csv file to Program
	#print len(giftsList)				

	for girl in girlsList:						# The loop assigns bf's to girls in the same order as the input
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
		logging.info("%s >>>boy %s is gifting gifts %s to girl %s" %(str(datetime.now()), boy.name, str(giftBasket), girl.name))
		boy.setHappiness()
		couple.happiness = girl.happiness + boy.happiness
		couple.compatibility = (boy.budget - girl.maintainenceBudget) + math.fabs(boy.attractiveness - girl.attractiveness) + math.fabs(boy.intelligenceLevel - girl.intelligenceLevel)



	k = int(raw_input("Enter Value of k >> "))		# Now User Enters Value of k
	
	#----------------------------Breakup After Valentines Day----------------------------------#

	j = 0
	print "Performing breakup of %d least happy Couples and assigning new boyfriends to the girls" %k								
	for couple in sorted(couplesList, key = lambda x : x.happiness, reverse = False): # the loop sorts the couples in the decreasing order of
		couple.boy.performBreakup()
		couple.girl.performBreakup()
		print "%s and %s just broked up" %(couple.boy.name, couple.girl.name)
		girl = couple.girl
		couplesList.remove(couple)
		for boy in boysList:
			if girl.canDateThisBoy(boy) and boy.canDateThisGirl(girl):
				if (boy.name not in girl.exbfs):
					girl.getCommitted(boy)
					boy.getCommitted(girl)
					logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt
					print "%s and %s just got committed" %(boy.name, girl.name)
		j += 1
		if j == k:
			break


