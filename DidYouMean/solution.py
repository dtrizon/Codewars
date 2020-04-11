def find_most_similar(word):
	finalAnswer = ""
	tempAnswer = ""
	highScore = 0
	for perword in ['Galman', 'Bolar']:
		scoreCounter = 0
		if finalAnswer == "":
			finalAnswer = tempAnswer = perword
		else:
			tempAnswer = perword
		if (len(word) <= len(perword)):
			for letterPos in range(0, int(len(word) / 2) + 1):
				if (word[letterPos] == perword[letterPos]):
					scoreCounter += 1
			for letterPos in range(len(word) - 1, int(len(word) / 2) + 1 , -1):
				if (word[letterPos] == perword[letterPos]):
					scoreCounter += 1
			if scoreCounter > highScore:
				finalAnswer = perword
				highScore = scoreCounter
		else:
			for letterPos in range(0, int(len(perword) / 2) + 1):
				if (word[letterPos] == perword[letterPos]):
					scoreCounter += 1
			for letterPos in range(len(perword) - 1, int(len(perword) / 2) + 1, -1):
				if (word[letterPos] == perword[letterPos]):
					scoreCounter += 1
			if scoreCounter > highScore:
				finalAnswer = perword
				highScore = scoreCounter
	return finalAnswer



find_most_similar('BHolar')


#https://www.codewars.com/kata/5259510fc76e59579e0009d4/train/python

#continue this one