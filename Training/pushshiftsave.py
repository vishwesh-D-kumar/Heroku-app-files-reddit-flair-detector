
import requests
import json
import time
import pymongo
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import praw

reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')
attributes_list=['created_utc','score','selftext','is_video',"title",
'over_18','num_comments','is_reddit_media_domain','num_crossposts','is_self']
stop_words = set(stopwords.words('english'))
def process_word(text):
	text=word_tokenize(text)
	return[i for i in text if i.isalpha() and i not in stop_words ]

urllist=[]
size=500
reqs_num=0
# epoch_aftertime=1563344188
epoch_beforetime=1563344188
# epoch_beforetime=1332004895
# 'https://api.pushshift.io/reddit/search/submission/?q=screenshot&after=1514764800&before=1517443200&subreddit=PS4'
url='https://api.pushshift.io/reddit/search/submission/?'+'&before='+str(epoch_beforetime)+'&subreddit=india&size=500'
# url='https://api.pushshift.io/reddit/search/submission/?after='+str(epoch_aftertime)+'&before='+str(epoch_beforetime)'&subreddit=india&size=500'
starttime=time.time()
print(url)
reqdata=requests.get(url)
data=json.loads(reqdata.text)
print(len(data['data']))
print(data['data'][-1]['created_utc'])
epoch_beforetime=data['data'][-1]['created_utc']
reqs_num+=1

# print(urllist)
completedataset=[]
while(len(completedataset))<1000:
	for i in data['data']:
		print(len(completedataset),"###")
		urllist.append(i['full_link'])
		completedataset.append(i)
		# print(len(i.keys()))
		# print(urllist[-1])

		submission=reddit.submission(url=urllist[-1])
		for i in attributes_list:
			completedataset[-1][str(i)]=getattr(submission,i)
		completedataset[-1]['created_utc']=int(completedataset[-1]['created_utc'])
		completedataset[-1]['selftext']=process_word(submission.selftext)
		completedataset[-1]['link_flair_text']=submission.link_flair_text
		# completedataset[-1]['distinguished']=str(submission.distinguished)
		completedataset[-1]['title']=process_word(submission.title)
		completedataset[-1]['comment_text']=[]
		completedataset[-1]['net_comment_score']=0
		if str(submission.link_flair_text)=='None' or len(completedataset[-1]['title'])<2 or completedataset[-1]['num_comments']<2 :
			completedataset.pop(-1)
			continue

		for comment in submission.comments:
			try:
				comment_text=comment.body
				completedataset[-1]['comment_text'].append(process_word(comment_text))
			except:
				continue
			completedataset[-1]['net_comment_score']+=comment.score
		if epoch_beforetime>completedataset[-1]['created_utc']:
			epoch_beforetime=completedataset[-1]['created_utc']
		# urllist.pop(-1)

	if reqs_num>119 and time.time()-starttime<60:
		time.sleep(60)
		starttime=time.time()
	# print(url)
	url='https://api.pushshift.io/reddit/search/submission/?'+'&before='+str(epoch_beforetime)+'&subreddit=india&size=500'
	print(url)
	reqdata=requests.get(url)
	data=json.loads(reqdata.text)
	epoch_beforetime=data['data'][-1]['created_utc']
	reqs_num+=1

attributes_list+=['link_flair_text','comment_text','net_comment_score']				
df=pd.DataFrame()
# df.columns=[i.keys for i in completedataset]
import pandas as pd
import nltk
# df=pd.read_csv('First_data200.csv')
for data_submission in completedataset:
	df=df.append([[data_submission[i] for i in attributes_list]])

df.columns=attributes_list
print(df)
print(epoch_beforetime)




# df.to_csv('First_data1000.csv')
df.to_pickle('Pickle1.pkl')
# print(epoch_beforetime)




# for url in urllist:
# 	submission=reddit.submission(url)
# 	submission=[]
# 	submission.







