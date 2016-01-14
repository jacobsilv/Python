import math
import sys

class case_selector(Exception):
   def __init__(self, value): # overridden to ensure we've got a value argument
      Exception.__init__(self, value)

def switch(variable):
   raise case_selector(variable)

def case(value):
   exclass, exobj, tb = sys.exc_info()
   if exclass is case_selector and exobj.args[0] == value: return exclass
   return None

def multicase(*values):
   exclass, exobj, tb = sys.exc_info()
   if exclass is case_selector and exobj.args[0] in values: return exclass
   return None




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





def bin_to_dec(binary):

	rev = binary[::-1]
	total=0
	for i in range(len(rev)):
		total+= math.pow(2,i)*int(rev[i])
	return total
	

def hex_to_dec(hex):
	rev = hex[::-1]
	total=0
	for i in range(len(rev)):
		try:
			switch(rev[i])
		except multicase(0,1,2,3,4,5,6,7,8,9):
			total+= math.pow(16,i)*int(rev[i])
		except case('a'):
			total+= math.pow(16,i)*10
		except case('b'):
			total+= math.pow(16,i)*11
		except case('c'):
			total+= math.pow(16,i)*12
		except case('d'):
			total+= math.pow(16,i)*13
		except case('e'):
			total+= math.pow(16,i)*14
		except case('f'):
			total+= math.pow(16,i)*15
	return total



def hex_to_dec_other(hex):
	rev = hex[::-1]
	total=0
	for i in range(len(rev)):
		if rev[i]=='a':
			total+= math.pow(16,i)*10
		elif rev[i]=='b':
			total+= math.pow(16,i)*11
		elif rev[i]=='c':
			total+= math.pow(16,i)*12
		elif rev[i]=='d':
			total+= math.pow(16,i)*13
		elif rev[i]=='e':
			total+= math.pow(16,i)*14
		elif rev[i]=='f':
			total+= math.pow(16,i)*15
		else:
			total+= math.pow(16,i)*int(rev[i])
	return total






if __name__=='__main__':
	answer = raw_input("yes enter a number to be converted: ")

	print "binary: " +binary(int(answer))
	print "hexidecimal: " +hexer(int(answer))

	print bin_to_dec("111")
	print hex_to_dec("af")
