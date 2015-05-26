import praw
import pprint



r = praw.Reddit(user_agent = "Top buildapcsales submissions by /u/topgearsad")
submissions = r.get_subreddit('buildapcsales').get_new(limit=10)

#Accesses object submissions property of '.title' which is the title of submission

for sub in submissions:
	if "[CASE]" in str(sub.title):
		print sub.title


	#for x in sub.title:
		 #pprint.pprint(str(x))






		
	#if sub.title == '[HDD] 2x3TB Seagate Barracuda ST3000DM001 ($91.00 each + 10% off with code CCEX052215 = $163.80, free shipping)':
		#print "Great Scott!"

	#print thing.title - Used to test accessing object items?
	#pprint.pprint(vars(thing)) - REALLY IMPORTANT!!!! Will print object items to access
