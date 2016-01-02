
import os, sys

dir = './'



'''
This is my reverse string method

'''
def rev1(word):
	leng = len(word)
	string = ""
	for i in range(0, len(word)):
		#grab the end of the string and go to the beginnning
		string+=word[leng-i-1]

	return string



#tester to make sure the correct chars were in place
def rev(word):
	leng = len(word)
	for i in range(0, len(word)):
		print word[leng-i-1],


rev("hello")
print "\n"
print rev1("hello")


'''
This method has an inputfile that is the file
you are reversing
'''
def filemaker(input_file):
	file_out = open("output.txt", 'w')
	print input_file

	for infile in os.listdir(dir):
		
		if infile == str(input_file):

			file_in = open(infile, 'r')

			for line in file_in:
				file_out.write(rev1(line))

			file_out.write("\n")
			
			file_in.close()
	file_out.close()




filemaker(str(sys.argv[1]))
