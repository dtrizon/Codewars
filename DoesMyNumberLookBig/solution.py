def narcissistic( value ):
    # Code away
    temp = 0
    for perNum in str(value):
	    temp += int(perNum) ** len(str(value))
    if value == temp:
        return True
    else:
        return False