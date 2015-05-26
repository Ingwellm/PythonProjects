import praw

#NEED TO DO:  Add list that can be updated and then ran against

r = praw.Reddit(user_agent = "Top buildapcsales submissions by /u/topgearsad")
submissions = r.get_subreddit('buildapcsales').get_new(limit=10)

#Accesses object submissions property of '.title' which is the title of submission.  By default this is in unicode...so I forced it to string

for sub in submissions:
	if "[CASE]" in str(sub.title):
		print sub.title

#pprint.pprint(vars(thing)) - REALLY IMPORTANT!!!! Will print object items to access
