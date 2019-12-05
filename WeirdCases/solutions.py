def to_weird_case(string):
    tempString = ""
    for word in string.split():
    	for char in range(0, len(word)):
    		if word[char] == " ":
    			tempString += " "
    			continue
    		elif char % 2 == 0:
    			tempString += f"{word[char].upper()}"
    		else:
    			tempString += f"{word[char]}"
    	tempString += " "
    return tempString.strip()