def unique_in_order(iterable):
	if iterable == '':
		return []
	else:
		tempString = [iterable[0]]

	for char in iterable[1::]:
		if tempString[-1] != char:
			tempString.append(char)
	return tempString




print(unique_in_order(''))
