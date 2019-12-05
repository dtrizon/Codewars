def solution(number):
	tempNum = 0
	for currnum in range(1, number):
		if (currnum % 3 == 0) | (currnum % 5 == 0):
			tempNum += currnum
	return tempNum

print(solution(10))