'''
Output
Each method will return a string value.

How It Works
Encoding and decoding are done by performing a series of character and substring rotations on a string input.

Encoding: The number of rotations is determined by the value of n. The sequence of rotations is applied in the following order:
 Step 1: remove all spaces in the string (but remember their positions)
 Step 2: shift the order of characters in the new string to the right by n characters
 Step 3: put the spaces back in their original positions
 Step 4: shift the characters of each substring (separated by one or more consecutive spaces) to the right by n
Repeat this process until it has been completed n times in total.
The value n is then prepended to the resulting string with a space.

Decoding: Decoding simply reverses the encoding process.
'''
string = "If you wish to make an apple pie from scratch, you must first invent the universe."
newString = [x in char]
spacePosition = []

for charPos in range(0, len(string)):
	#print(string[charPos])
	if string[charPos] == " ":
		spacePosition.append(string[::charPos].index(string[charPos]) + charPos - 1)
