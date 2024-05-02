

import math
from datetime import date

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
namesOfMonths = ["Jan", "Fab", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def makeSets(sets, start, end):
	itemsPerSet = math.ceil((end - start + 1) / 2)
	numberOfSets = math.ceil(math.log((end - start + 1), 2))
	
	for i in range(numberOfSets):
		sets.append(list([2**i + start - 1]))
		steps = 2**i - 1
		numToAdd = 2**i + 1
		
		while len(sets[i]) < itemsPerSet:
			if steps > 0:
				sets[i].append(sets[i][len(sets[i]) - 1] + 1)
				steps -= 1
			elif steps == 0:
				sets[i].append(sets[i][len(sets[i]) - 1] + numToAdd)
				steps = 2**i - 1
		
		for j in range(len(sets[i])):
			if sets[i][j] > end:
				sets[i][j] = "*"

def displaySets(sets, name):
	birth = 0
	answer = 0
    
	elementsPerLine = math.ceil(math.sqrt(len(sets[0])))
	spaces = math.floor(49 / (elementsPerLine + 1))
	
	line = ""
	
	for i in range(len(sets)):
		line = " " * spaces
		for j in range(len(sets[0])):
			if j + 1 == len(sets[0]):
				line += format(str(sets[i][j]), f"<{spaces}s")
				line += format("*", f"<{spaces}s") * (elementsPerLine - 1)
				print(line)
				print()
				elementsPerLine = math.ceil(math.sqrt(len(sets[0])))
				line = ""
			
			else:
				line += format(str(sets[i][j]), f"<{spaces}s")
				elementsPerLine -= 1
			
			if elementsPerLine == 0:
				print(line)
				line = " " * spaces
				print()
				elementsPerLine = math.ceil(math.sqrt(len(sets[0])))
		
		answer = eval(input(f"Enter 1 if your {name} of birth in this set, 0 if not: "))
		
		if answer == 1:
			birth += 2 ** i
		print()
		
	birth += (sets[0][0] - 1)
	return birth

def countAge(dayOfBirth, monthOfBirth, yearOfBirth, months, namesOfMonths):
	currentYear, currentMonth, currentDay = map(int, str(date.today()).split("-"))
	
	days = months[monthOfBirth] - dayOfBirth
	days += currentDay
	
	months = 12 - monthOfBirth
	months += currentMonth - 1
	
	years = (currentYear - yearOfBirth) - 1
	
	if days >= 30:
		months += 1
		days -= 30
        
	if months >= 12:
		years += 1
		months -= 12
		
	print(f"You are {years} years {months} months {days} days!")

setsOfDays = list()
setsOfMonths = list()
setsOfYears = list()

makeSets(setsOfDays, start = 1, end = 31)
makeSets(setsOfMonths, start = 1, end = 12)
makeSets(setsOfYears, start = 1941, end = 2004)

dayOfBirth = displaySets(setsOfDays, "day")
monthOfBirth = displaySets(setsOfMonths, "month")
yearOfBirth = displaySets(setsOfYears, "year")

print("You were born in ", dayOfBirth, namesOfMonths[monthOfBirth - 1], yearOfBirth)
print()

countAge(dayOfBirth, monthOfBirth, yearOfBirth, months, namesOfMonths)
  
