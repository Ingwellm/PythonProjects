#File open and check if Pallindrome
# location = raw_input("Enter location of file ")

# def is_pallindrome(x):
	# f = open(location).read().split('\n')
	# for lines in f:
		# if lines == lines[::-1]:
			# print "%s is a pallindrome" % lines
		# else:
			# print "%s is not a pallindrome" % lines
# is_pallindrome(list)


from collections import Counter
#Prompts users for location of file
location = raw_input("Enter location of file ")


def char_freq_table(x):
	f = open(location).read().split('\n') #Opens file and removes nobreakspace from end of line
	for chars in f:
		a =  Counter(chars)
		sor = sorted(a.keys()) #Sorts the list by keys
		for key in sor:        #Iterates over keys and prints them out sorted
			print (key, a[key]), #Comma prints horizontal, taking it away prints vertical
								
char_freq_table(list)


		
