import nltk 
import pandas as pd
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
# df=pd.read_pickle('Unpolarized_dataset.pkl')
df=pd.read_pickle('Pickle2.pkl')
# df=pd.concat([pd.read_pickle('Pickle1.pkl'),pd.read_pickle('Pickle2.pkl'),pd.read_pickle('Unpolarized_dataset.pkl')])
print(df.columns)
# df.loc[i,'num_comments']
from collections import Counter
# allowed_flairs=['AMA','Science/Technology','Food', 'Demonetization', 'Photography', 'Policy & Economy','[R]eddiquette','Non-Political','Sports','AskIndia','Politics']
allowed_flairs=list(set(df.link_flair_text.values))
##############INFO(TEXT)###########
'''
Top words top subs['India', 'I', 'Indian', 'The', 'This', 'A', 'Mumbai', 'NP', 'first', 'today', 'Delhi', 'one', 'people', 'My', 'made', 'Modi', 'like', 'get', 'years', 'Kerala', 'old', 'It', 'Bangalore', 'found', 'time', 'day', 'OC', 'In', 'new', 'police', 'Hyderabad', 'two', 'Chennai', 'help', 'year', 'life', 'last', 'picture', 'days', 'Indians', 'How', 'need', 'see', 'TIL', 'got', 'photo', 'friend', 'took', 'He', 'team']
Top words latest subs['India', 'I', 'Indian', 'What', 'How', 'The', 'Is', 'In', 'help', 'A', 'get', 'Rs', 'Why', 'people', 'good', 'advice', 'Need', 'Delhi', 'BJP', 'Mumbai', 'life', 'anyone', 'World', 'Can', 'Assam', 'Help', 'state', 'first', 'years', 'would', 'need', 'job', 'As', 'To', 'time', 'like', 'Indians', 'Singh', 'Kerala', 'students', 'On', 'man', 'Any', 'many', 'Please', 'says', 'one', 'day', 'think', 'Congress']
'''

def timegraph(attribute):
	allowed_flairs

######WordCloud
def word_cloud(flair):
	global df

	BoWTitles=[]
	# for j in df.comment_text.values:
	# 	for i in j:
	# 		BoWTitles+=i

	for i in range(len(df)):
		if df.loc[i,'link_flair_text']==flair:
			BoWTitles+=df.loc[i,'title']

	frequency_dist = nltk.FreqDist(BoWTitles)
	print(sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50])
	#Removing  stop words for processing 
	try:
		baka=sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]
		wordcloud = WordCloud().generate_from_frequencies(frequency_dist)
		plt.imshow(wordcloud)
		plt.axis("off")
		if flair=='Science/Technology':
			flair='Science&Technology'
		plt.savefig('BrownieImages/AllFlairsTopWords/'+flair)
		plt.show()
	except:
		return

def doc_generator(flair):
	doc=''
	for i in range(len(df)):
		if df.loc[i,'link_flair_text']==flair:
			for word in df.loc[i,'title']:
				doc+=word
	return doc
for flair in allowed_flairs:
	docs=[]



"""
If you use the VADER sentiment analysis tools, please cite:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score
flair_score={}
# df=df.reset_index()
for i  in allowed_flairs:
	flair_score[i]=0
flair_nums=Counter(df.link_flair_text.values)
print(flair_nums)
for i in range(len(df)):
	# s=''
	# for j in df.loc[i,'title']:
	# 		s+=j+" "


	flair_score[df.loc[i,'link_flair_text']]+=df.loc[i,'score']
	# flair_score[df.loc[i,'link_flair_text']]+=df.loc[i,'num_comments']

for i in flair_score.keys():
	print(i)
	try:
		flair_score[i]/=flair_nums[i]
	except:
		continue
# # for flair in allowed_flairs:
# 	word_cloud(flair)
explode=[0]*len(flair_score.keys())
# print(flair_score)
for i in range(len(list(flair_score.keys()))):
	print("<p>flair"+str(i)+"-->"+list(flair_score.keys())[i]+"</p>")
	if list(flair_score.keys())[i]=='r/all':
		explode[i]=0.1


# explode[2]=0.2
plt.title('Share of votes in flairs')
# plt.bar(["flair"+str(i) for i in range(len(list(flair_score.keys())))],list(flair_score.values()))
plt.pie(list(flair_score.values()),labels=list(flair_score.keys()),autopct='%0.0f%%',
        shadow=True,explode=explode)

# plt.title('Sentiment Analysis of Comments')
plt.savefig('BrownieImages/score',transparent=True)
# plt.savefig('BrownieImages/gildings')
plt.show()


