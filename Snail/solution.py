array = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12]]

maxMovement = len(array) * len(array[0])
currMovement = 0
print(maxMovement)

'''for perRowHeight in range(0, len(array)):
	for perColumn in range(0, len(array[perRowHeight])):
		if (perRowHeight == 0) or (perRowHeight == len(array) - 1):
			print(array[perRowHeight][perColumn])
		elif '''


baseX = 3
baseY = 4
maxMove = baseX * baseY
currmov =0
listofmoves = []

while currmov < maxMove:
	for y in range(0, baseY):
		if y == 0:
			listofmoves.append([x for x in range(1, baseX + 1)])
			currmov += baseX
		elif y == baseY - 1:
			listofmoves.append([x for x in range(maxMove, maxMove - baseX, -1)])
			currmov += baseX
		currmov += 1

print(listofmoves)


[1,2,3],
[4,5,6],
[7,8,9]	



