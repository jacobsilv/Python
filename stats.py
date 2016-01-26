import math

array= [8.0,11.0,0.0,4.0,7.0,8.0,10.0,5.0,8.0,3.0]

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
	for i in range(0, len(array)):
		sum += array[i]

	return float(sum)/float(len(array))


def variance(data):

	length = len(data)
	df = length - 1

	sumsqrt = 0
	sqrtsum = 0

	for integer in range(0,len(data)):
		sumsqrt += data[integer] *data[integer]
		sqrtsum += data[integer]

	sqrtsum *= sqrtsum

	result = (sumsqrt - (sqrtsum/length))/df

	return result


def sd(variance):

	return math.sqrt(variance)



def t_value(array, sd, pop_ave):

	result = (mean(array)-pop_ave)/(sd/math.sqrt(len(array)))
 	return result




# run the methods for all the statistics

print "Mean: "+str(mean(array))
print "Median: "+str(median(array))
print "Mode: "+str(mode(array))


print "Standard Deviation: "+str(sd(variance(array)))
print "Variance: "+str(variance(array))


pop = raw_input("please enter the population average: ")
print "t value: ",
print str(t_value(array, sd(variance(array)), float(pop)))

