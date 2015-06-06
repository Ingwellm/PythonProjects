import praw

#NEED TO DO:  Add list that can be updated and then ran against
look_for_these_deals = ['XB270HU'. '1440']
title_to_look_at = submissions.sub.title #Is this correct?

r = praw.Reddit(user_agent = "Top buildapcsales submissions by /u/topgearsad")
subreddit = r.get_subreddit('buildapcsales')
submissions = subreddit.get_new(limit=10)

#Accesses object submissions property of '.title' which is the title of submission.  By default this is in unicode...so I forced it to string

for sub in submissions:
	if look_for_these_deals in str(sub.title):
		print sub.title
	else:
		print "These are not the deals you are looking for"

#pprint.pprint(vars(thing)) - REALLY IMPORTANT!!!! Will print object items to access
