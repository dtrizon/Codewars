orderNum = [1, 5, 10, 50,100, 500, 1000]
roman = ["I","V","X","L","C","D","M"]

total = 0
for charPos in range(0, len(inputRoman)):
	if inputRoman[charPos] not in roman:
		break
	else:
		if (charPos != 0) and (roman.index(f"{inputRoman[charPos - 1]}") < roman.index(f"{inputRoman[charPos]}")):
			#print(orderNum[roman.index(inputRoman[charPos - 1])])
			total += orderNum[roman.index(inputRoman[charPos])] - orderNum[roman.index(inputRoman[charPos - 1])]
			total -= orderNum[roman.index(inputRoman[charPos-1])]
		else:
			total += orderNum[roman.index(inputRoman[charPos])]
return total