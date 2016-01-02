import math

'''

def findSlope(x , string):
	slope = ""
	foundX = ""
	Yintercept = ""
	for i in range(len(string)):
		if (string[i] !="x" and foundX != "x"):
			slope+=string[i]
		else: 
			foundX = "x"

		if (foundX == "x" and string[i]!="x" and string[i] != "+"):
			Yintercept += string[i]

	print int(slope)*x+int(Yintercept)

'''





'''
Takes in an array of data
then it prints the important info
no return
'''
def stats(data):
	
	print "average " + str(sum(data)/len(data))


	length = len(data)
	df = length - 1


	sumsqrt = 0
	sqrtsum = 0

	for integer in range(0,len(data)-1):
		sumsqrt += data[integer] ** 2
		sqrtsum += data[integer]

	sqrtsum = sqrtsum**2

	result = (sumsqrt + (sqrtsum/length))/df


	print "variance",
	print result

	print "Standard Deviation",
	print math.sqrt(result)




array= [1, 4, 2, 5]

array.sort()


def mode(array):
	return array[len(array)-1]

def median(array):
	if len(array)%2==0:
		return (array[(len(array)-1)/2]+array[(len(array))/2])/2
	else:
		return array[(len(array)-1)/2]

def mean(array):
	sum=0
	for i in range(0, len(array)-1):
		sum += array[i]

	return float(sum)/len(array)




print mean(array)
print median(array)
print mode(array)



'''
string = raw_input("please enter your function: ")
findSlope(7, string)
x = 7
'''

stats([5.0, 7.0, 3.0, 2.0])





 
