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
import random

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
	logging.basicConfig(filename='q7Log.txt',level=logging.DEBUG)			
	boysList, girlsList, giftsList, couplesList = [], [], [], []		
	loadData()				 			#calls the function which loads data from csv file to Program
	#print len(giftsList)				

	for girl in sorted(girlsList, key = lambda x : x.attractiveness, reverse = True):						# The loop assigns bf's to girls in the same order as the input
		for boy in boysList:
			if girl.canDateThisBoy(boy) and boy.canDateThisGirl(girl):
				girl.getCommitted(boy)
				boy.getCommitted(girl)
				couplesList.append(Couple(girl, boy))
				logging.info("%s >>>girl %s got committed with Boy %s" %(str(datetime.now()), girl.name, boy.name)) # Logs TimeStamp and Committments into q1Log.txt

	algo = int(raw_input("Enter the choice of data structure in which you want to store the committed boys 1 for list, 2 for hash Table, 3 for sorted Array------>"))
	
	randomBoyList = boysList[100:200]

	if algo == 1:
		arr = []
		for couple in couplesList:
			arr.append(couple.girl.name)
		for x in randomBoyList:
			for couple in couplesList:
				if couple.boy.name == x.name:
					if couple.girl.name in arr:
						print "%s's gf's name is %s" %(x.name, couple.girl.name)
					break
			else:
				print "%s is single" %(x.name)
	elif algo == 2:
		arr = {}
		for couple in couplesList:
			arr[couple.boy.name] = couple.girl.name
		for x in randomBoyList:
			if x.name in arr:
				print "%s's gf's name is %s" %(x.name, arr[x.name])
			else:
				print "%s is single" %x.name
	elif algo == 3:
		arr = []
		for couple in couplesList:
			arr.append(couple.girl.name)
		arr.sort()
		for x in randomBoyList:
			for couple in couplesList:
				if couple.boy.name == x.name:
					if couple.girl.name in arr:
						print "%s's gf's name is %s" %(x.name, couple.girl.name)
					break
			else:
				print "%s is single" %(x.name)







