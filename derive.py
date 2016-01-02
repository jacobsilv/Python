
import re

function = "2x^1+3x^4+16x^4-1"



def deriveString(function):

	arrayPlusMinus = []

	if "+" in function:
		for i in range(0,len(function)):
			if function[i] == "+":
				arrayPlusMinus.append("+")

			if function[i] == "-":
				arrayPlusMinus.append("-")


		array = []

		array = re.split("\+|\-", function)


	 	count = 0

		for var in array:

			if "^" in var:

				varArray = []

				varArray = var.split("^")


				number = varArray[1]

				varArray[1] = str(int(varArray[1])-1)

				if hasNumbers(varArray[0]):
					firstNumber = re.findall(r'\d+', varArray[0])
					number = int(firstNumber[0])*int(number)
					number = str(number)


				var = number +"x" +"^"+varArray[1]

				array[count] = var


			elif "^" not in var:
				if var == "x":
					array[count] = "1"
				else:
					array[count] = "0"

			count += 1


		for i in range(0,len(array)):
			
			if i == len(array)-1:

				print array[i]

			else :

				print array[i] + " "+arrayPlusMinus[i], 


	elif function == "x":

		print 1


	else:

		array = []


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)




if __name__ == "__main__":
	deriveString(function)
