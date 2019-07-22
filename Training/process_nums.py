import pandas as pd
from  sklearn.metrics  import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")

# df=pd.read_pickle('Pickle1.pkl')
dataframes=['Unpolarized_dataset.pkl','Pickle1.pkl','Pickle2.pkl']
for pkl in dataframes:
	print("-----------",pkl,"DATAFRAME Under Consideration---------")
	df=pd.read_pickle(pkl)
	df = df.sample(frac=1).reset_index(drop=True)
	# print(df)

	def clean_flairs():
		df=df.reset_index()
		allowed_flairs=['AMA','Science/Technology','Food', 'Demonetization', 'Photography', 'Policy & Economy','[R]eddiquette','r/all','Non-Political','Sports','AskIndia','Politics']
		flair_map={}
		c=0
		for i in allowed_flairs:
			flair_map[i]=c
			c+=1
		print(df.columns)
		print(set(df['link_flair_text']))
		x=list(df['link_flair_text'].values)
		y=[]
		for i in range(len(x)):
			if x[i] not in allowed_flairs:

				for j in allowed_flairs:
					if x[i].find(j)!=-1:
						x[i]=j
						break
				if x[i].find(j)==-1:
					df.drop(i,inplace=True)
					x[i]='Removethis'
		for i in x:
			if i!='Removethis':
				y.append(i)
		df=df.reset_index()
		print(len(y),len(df))
		df['link_flair_text']=y


		# df.to_pickle('Pickle1.pkl')

	#####Preprocessing flairs to become numeric

	le = preprocessing.LabelEncoder()
	y=le.fit_transform(list(df.link_flair_text.values))

	numeric_cols=['created_utc','score','num_comments','num_crossposts','net_comment_score']
	# numeric_cols=['num_crossposts','net_comment_score']

	for lol in numeric_cols:
		x=[]
		print("--Attribute-- "+lol)
		numeric_cols2=[lol]
		for i in range(len(df)):
			x.append([])
			for attr in numeric_cols2:
				x[i].append(df.loc[i,attr])
		# print(x[:5])
	# x=list(zip(tuple(x)))

		X_train, X_test, y_train, y_test = train_test_split(x,y ,test_size=0.15, random_state=42)
		clf=LinearSVC()
		clf.fit(X_train,y_train)
		predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
		try:
			clf=MultinomialNB()
			clf.fit(X_train,y_train)
			predicted=clf.predict(X_test)
			print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
		except:
			print("MultinomialNB left , attribute is negative")
		clf=SGDClassifier()
		clf.fit(X_train,y_train)
		predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
		clf=RandomForestClassifier()
		clf.fit(X_train,y_train)
		predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
		clf=LogisticRegression()
		clf.fit(X_train,y_train)
		predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))







