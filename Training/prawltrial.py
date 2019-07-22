import praw
import datetime as dt
reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')
# subreddit = reddit.subreddit('india')
# submissions=subreddit.top(limit=10)

# for submission in submissions: 
# 	print(submission.link_flair_text,submission.title)
	# print(submission.author.gilded)

id=input()
print(reddit.submission(id=id).link_flair_text)



