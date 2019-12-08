def solution(string,markers):
	return "".join([char for char in string if char not in markers]).replace('  ', ' ')



string = "a #b\nc\nd $e f g"
markers = ["#", "$"]
print(solution(string, markers))