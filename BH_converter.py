def binary(y):
	rem = 0
	array = []
	string = ""
	while (y != 0 ):
		rem = y%2
		array.append(rem)
		y=y/2

	array = array[::-1]
	for i in range(len(array)):
		string+= str(array[i])
	return string


def hexer(x):
	alph = ['a', 'b', 'c', 'd', 'e', 'f']
	rem = 0
	array = []
	string ="0x"

	while (x != 0):
		rem = x %16
		array.append(rem)
		x = x /16

	array = array[::-1]
	for i in range(len(array)):
		if (array[i]>9):
			string+= alph[array[i]-10]
		else:
			string+= str(array[i])
	return string

answer = raw_input("yes enter a number to be converted: ")

print "binary: " +binary(int(answer))

print "hexidecimal: " +hexer(int(answer))
