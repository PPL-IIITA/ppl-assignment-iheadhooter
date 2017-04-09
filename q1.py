import csv, logging
from datetime import datetime
from Boy import Boy
from Girl import Girl
from Couple import Couple
import utilities



def loadData():   										# Loads Data from CSV into Program
	global boysList, girlsList, giftsList

	try:
		with open('randomBoys.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				boysList.append(Boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5]))
			csvfile.close()
	except:
		pass

	try:
		with open('randomGirls.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				girlsList.append(Girl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4], row[5]))
			csvfile.close()
	except:
		pass

	try:
		with open('randomGifts.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				giftsList.append(Gift(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
			csvfile.close()
	except:
		pass



if __name__ == '__main__':

	utilities.generateRandomItems()								# calls utitilty function to create random Data
	logging.basicConfig(filename='q1Log.txt',level=logging.DEBUG)				# 
	boysList, girlsList, giftsList, couplesList = [], [], [], []				
	loadData()										# loads Data from csv files into Program

	for girl in girlsList:									# the loops assigns boyfriends to girls in the same
		for boy in boysList:								# order as the input
			if girl.canDateThisBoy(boy) and boy.canDateThisGirl(girl):
				girl.getCommitted(boy)
				boy.getCommitted(girl)
				couplesList.append(Couple(girl, boy))
				logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt


	for couple in couplesList:								# prints the couples on Console 
		print "girl %s just got committed with Boy %s" %(couple.girl.name, couple.boy.name)


	


