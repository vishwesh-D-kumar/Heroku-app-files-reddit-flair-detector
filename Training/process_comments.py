##Processing Textual data
import pandas as pd
import nltk 
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from  sklearn.metrics  import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import praw
import warnings
warnings.filterwarnings("ignore")

reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')


dataframes=['Unpolarized_dataset.pkl','Pickle1.pkl','Pickle2.pkl']
faltudf=pd.read_pickle('Unpolarized_dataset.pkl')
# dataframes=['Unpolarized_dataset.pkl']
for pkl in dataframes:
	print("-----------",pkl,"DATAFRAME Under Consideration---------")
	df=pd.read_pickle(pkl)
	df=pd.concat([faltudf,df])
	print(len(df))
	df.drop_duplicates(subset=['created_utc'],keep='first',inplace=True) 
	print(len(df))
	df['title']=df['title']+df['selftext']
	# X_train = [str(i)+" " for i in df['title'].values]
	# y_train = df['link_flair_text'].values
	# X_test = [str(i)+" " for i in df['title'].values]
	# y_test = df['link_flair_text'].values
	X_train, X_test, y_train, y_test = train_test_split([str(i)+" " for i in df['title'].values], df['link_flair_text'].values, test_size=0.15, random_state=42)

	vectorizer = TfidfVectorizer()
	X_train = vectorizer.fit_transform(X_train)
	X_test = vectorizer.transform(X_test)


	# for i in range(len(y_test)):
	# 	print(y_test[i],predicted[i])
	clf=LinearSVC()
	clf.fit(X_train,y_train)
	predicted=clf.predict(X_test)
	print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
	# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
	# try:
	clf=MultinomialNB()
	clf.fit(X_train,y_train)
	predicted=clf.predict(X_test)
	print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
	# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
	# except:
	# 	print("MultinomialNB left , attribute is negative")
	clf=SGDClassifier()
	clf.fit(X_train,y_train)
	predicted=clf.predict(X_test)
	print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
	# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
	clf=RandomForestClassifier()
	clf.fit(X_train,y_train)
	predicted=clf.predict(X_test)
	print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
	# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
	clf=LogisticRegression()
	clf.fit(X_train,y_train)
	predicted=clf.predict(X_test)
	print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
	# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))


