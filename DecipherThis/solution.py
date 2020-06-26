def encrypt_this(s):
	r = ""
	for x in s.split(' '):
		# x // string
		z = ""
		for y in range(0, len(x)):

			if y == 0:
				z += str(ord(x[0]))
			elif y == 1:
				z += x[-1]
			elif (y == len(x) - 1):
				z += x[1]
			else:
				z += x[y]
		r += z + " "
	return r[:-1]

print(encrypt_this("Hello good day"))
