from random import randrange
import csv

def generateRandomItems():

	"""generates 1000 X random boys, 500 X random girls, 1000 X random gifts and store them in csv format"""

	target = open('randomBoys.csv', 'w')
	writer = csv.writer(target, delimiter = ',')
	for k in range(1000):
		temp = ['Boy' + str(k), randrange(100), randrange(100), randrange(100), randrange(100)]
		x = randrange(100) % 3
		if x == 0:
			trait = 'miser'
		elif x == 1:
			trait = 'generous'
		else:
			trait = 'geek'
		temp.append(trait)
		writer.writerow(temp)
	target.close()


	target = open('randomGirls.csv', 'w')
	writer = csv.writer(target, delimiter = ',')
	for k in range(500):
		temp = ['Girl' + str(k), randrange(100), randrange(100), randrange(100)]
		x = randrange(100) % 3
		if x == 0:
			choosingCriteria = 'attractive'
		elif x == 1:
			choosingCriteria = 'rich'
		else:
			choosingCriteria = 'intelligent'

		x = randrange(100) % 3
		if x == 0:
			trait = 'choosy'
		elif x == 1:
			trait = 'normal'
		else:
			trait = 'desperate'

		temp.extend([choosingCriteria, trait])
		writer.writerow(temp)
   	target.close()

   	target = open('randomGifts.csv', 'w')
   	writer = csv.writer(target, delimiter = ',')
   	for k in range(1000):
   		temp = []
   		x = randrange(100) % 3
   		if x == 0:
   			type = 'essential'
   		elif x == 1:
   			type = 'luxury'
   		else:
   			type = 'utility'
   		temp.append(type)
   		temp.append(randrange(100))
   		temp.append(randrange(100))
   		temp.append(randrange(100))
   		temp.append(randrange(100))

   		writer.writerow(temp)
   	target.close()
