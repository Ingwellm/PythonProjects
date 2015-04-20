#File open and check if Pallindrome

def is_pallindrome(x):
	f = open('c:\pals.txt', 'r').read().split('\n')
	for lines in f:
		if lines == lines[::-1]:
			print "%s is a pallindrome" % lines
		else:
			print "%s is not a pallindrome" % lines
is_pallindrome(list)			
