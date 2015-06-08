#Password Generator

import string
import random

password_requirement = raw_input("For 8 character password type eight, for 8 character password complex type special, for 12 character simple type twelve, and for 12 character complex type complex: ")

numbers = str(random.randrange(10))
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
alpha_lists = [list(string.ascii_lowercase), list(string.ascii_uppercase)]
# i = random.randint(0,1)
# a = random.randint(0,25)






#print random.choice(alphabet_lowercase)
#print random.choice(alphabet_uppercase)
#print numbers
#print random.choice(special_characters)

def simple_eight():   #Below will choose one lowercase letter and make ten, at this point it is simply for testing so that it ends up with more than 8 chars and does not loop forever
    if password_requirement == 'eight':
		password = [0] * 4
		x = 0
		while x < 4:
			i = random.randint(0,1)
			a = random.randint(0,25)
			password[x] = alpha_lists[i][a] + numbers
			x += 1
    print "Your password is %s" % password
		
simple_eight()

# def complex_eight():
	# if password_requirement == 'special':

# def simple_twelve():
	# if password_requirement == 'twelve':

# def complex_twelve():
	# if password_requirement == 'complex':		

# def generate_password():

#i = 0
#password[i]
#while password < 8
#selector = 
#i = random index of list containing all sub-lists
#i += 1
#password = random.choice(alphabet_lowercase) + str(numbers) + (random.choice(alphabet_uppercase) * 6)