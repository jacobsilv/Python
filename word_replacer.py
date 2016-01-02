
def findAndReplace(originalString, stringToFind, stringToReplace):
	current_letter = 0

	
	if stringToFind in originalString:
		test = True
	else:
		test = False

	for i in range(len(originalString)-len(stringToFind)+1):
		count = 0
		for j in range(len(stringToFind)-1):

			if stringToFind[j] == originalString[i+j] and test==True:
				count+=1
			else:
				count = 0
			if j==len(stringToFind)-2 and count == len(stringToFind)-1 :
			
				originalString = originalString[0:i]+stringToReplace+originalString[i+len(stringToFind):]
	print originalString

	#print originalString


findAndReplace("practice round one not but maybe it will not work depending", "maybe", "legit")
