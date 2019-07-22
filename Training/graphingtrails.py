import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_pickle('Unpolarized_dataset.pkl')
import time
allowed_flairs=['AMA','Science/Technology','Food', 'Photography', 'Policy & Economy','[R]eddiquette','r/all','Non-Political','Sports','AskIndia','Politics']
df=pd.concat([pd.read_pickle('Pickle1.pkl'),pd.read_pickle('Pickle2.pkl'),pd.read_pickle('Unpolarized_dataset.pkl')])
df.drop_duplicates(subset=['created_utc'],keep=False,inplace=True) 
# df[['created_utc','link_flair_text']].plot()
# plt.show()
# df=df.reset_index()
def time_activity():
	c=0
	for flair in allowed_flairs:

		total=[0]*24
		print(df.loc[4])
		for i in range(len(df)):
			if df.loc[i,'link_flair_text']==flair:
				total[time.localtime(df.loc[i,'created_utc']).tm_hour]+=1
		# c+=1
		# plt.subplot(2,2,c)
		plt.title(flair)
		plt.plot(range(24),total)
		
		if flair=='Science/Technology':
			flair='Science and Technology'
		if flair=='r/all':
			flair='r and all'
		plt.savefig('BrownieImages/TimeAnalysis/'+flair+'.png')

		
		# plt.clf()
		plt.show()
		

# plt.savefig('/BrownieImages',transparent=True)
def comment_activity():
	flair_map={}
	for flair in allowed_flairs:
		flair_map[flair]=0
	for i in range(len(df)):
		print(df.loc[i,'num_comments'])
		flair_map[df.loc[i,'link_flair_text']]+=df.loc[i,'num_comments']
	plt.bar(flair_map.keys(),flair_map.values())
	plt.show()
comment_activity()




