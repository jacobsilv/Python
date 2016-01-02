#! /bin/python

import getpass
word = getpass.getpass('Word: ')



def hangman(word):
	answer = '%d %d %d %d %d %d %d '% (1, 2, 3, 4, 5, 6, 7)
	print answer
	tries = 1
	while tries <= 5:
		guess = raw_input('guess the word one letter at a time: ')
		#if len(guess)>1:
		#	guess = raw_input('try again: guess the word one letter at a time: ')
		if isinstance(guess, (int)):
			guess = raw_input('try again: guess the word one letter at a time: ')
		if guess in word:
			for i in range(len(word)):
				if word[i] == guess:
					answer = answer.replace("%d " % (i+1), guess, i+1)
					print answer
					if answer == word:
						print "you win"
			if answer == word:
				return True
		else:
			print "u have tried this many times %d you only get 5 tries" % (tries)
			tries += 1
	print "Better luck next time BITCH"


import webbrowser
def hangman1(word):
	answer = len(word) * '_'
	tries = 1
	guess_panal = []
	while tries <= 7:
		print answer
		guess = raw_input('guess the word one letter at a time: ')
		print "these are the letters you have tried: "
		if guess in word and not guess in guess_panal:
			guess_panal.append(guess)
			for i in range(len(word)):
				if word[i] == guess:
					ans_list = list(answer)
					ans_list[i] = guess
					answer = ''.join(ans_list)
					if answer == word:
						print "you win"
						webbrowser.open('http://www.keepcalm-o-matic.co.uk/p/keep-calm-and-you-win-5/')
			if answer == word:
				return True
		else:
			if guess in guess_panal:
				print "you tried that word"
			else:
				guess_panal.append(guess)
				print "u have tried this many times %d you only get 7 tries" % (tries)
				tries += 1
		print guess_panal
	print "Better luck next time"
	webbrowser.open('google.com')

	
if __name__ == "__main__":
	hangman1(word)

