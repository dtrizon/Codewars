def make_readable(seconds):
	formatString = [0, 0, 0]

	for perSec in range(0, seconds):
		formatString[2] += 1
		if (formatString[2] == 60):
			formatString[1] += 1
			formatString[2] = 0
		if(formatString[1] == 60):
			formatString[0] += 1
			formatString[1] = 0
	for item in range(0, len(formatString)):
		formatString[item] = str(formatString[item])
		if len(formatString[item]) == 1:
			formatString[item] = f"0{formatString[item]}"

	return f"{formatString[0]}:{formatString[1]}:{formatString[2]}"


print(make_readable(60))


# 60 seconds = 1 min
# 60 min     = 1 hr

#86399
#1,439.983333333333‬ MIN
#23.99972222222222 HR
