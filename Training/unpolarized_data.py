import pandas as pd
import praw
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
def process_word(text):
	text=word_tokenize(text)
	return[i for i in text if i.isalpha() and i not in stop_words ]
reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')
allowed_flairs=['AMA','Science/Technology','Food', 'Demonetization', 'Photography', 'Policy & Economy','[R]eddiquette','r/all','Non-Political','Sports','AskIndia','Politics']
attributes_list=['created_utc','score','selftext','is_video',"title",
'over_18','num_comments','is_reddit_media_domain','num_crossposts','is_self','link_flair_text']
df=pd.DataFrame()
for flair in allowed_flairs:
	print(flair)
	for submission in reddit.subreddit('india').search('flair:"'+flair+'"', limit=100):
		data=[]
		# print(submission.link_flair_text)
		for attr in attributes_list:
			if attr=='title' or attr=='selftext':
				data.append(process_word(getattr(submission,attr)))
				continue
			if attr=='link_flair_text':
				data.append(flair)
				continue
			data.append(getattr(submission,attr))
		data.append([])
		data.append(0)
		# for comment in submission.comments:
		# 	try:
		# 		comment_text=comment.body
		# 		data[-2].append(comment_text)

		# 	except:
		# 		continue
		# 	data[-1]+=comment.score
		print(data)
		df=df.append([data])
		print(df)


attributes_list+=['comment_text','net_comment_score']
df.columns=attributes_list
df=df.reset_index()
print(df)
df.to_pickle('Unpolarized_dataset.pkl')
print(df.columns)



