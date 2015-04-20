# Python Exercises

#15
def find_longest_word(x = [], *args):
	a = 0
	for i in x:
		if len x > a:
			x == a
		print a

#16
def filter_long_words(x = [], n, *args):
	for i in x:
		if i > n:
		print i

#17
def is_pallindrome(x):
	if x == x[::-1]
		print "Is pallindrome"
	else:
		print "Is not pallindrome"
	
	
#18
def pangram(x):
	for i in x:
		if i == "a", and "b", and "c", and "d", and "e":
			print "Is pangram"
		else:
			print "Is not pangram"

#19

#20

def translate(x = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}):
	for i in x:
		print i
		
#21
def char_freq(x):
		a = {i:x.count(i) for i in x}
		print a

#22
x = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
def rot(x):
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
	for i in x:
		for a in key.keys():
			if i == a:
				print key[a]
				
#23
import re
x = "This   is  very funny  and    cool.Indeed!"
#a = re.sub("\s\s+", " ", x)
a = " ".join(x.split())
print a
	
#24

#32
	
	
		
	   


	



	


	
		
	
	
	
