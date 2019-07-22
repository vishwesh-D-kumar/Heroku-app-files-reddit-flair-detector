##Checking Database accuracy on one another to pick best accuracy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from  sklearn.metrics  import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")


train_sets=['Pickle1.pkl','Pickle2.pkl']
test_set=['Unpolarized_dataset.pkl']
# test_set=['Unpolarized_dataset.pkl','Pickle2.pkl']
# train_sets=['Pickle1.pkl']
# faltudf=pd.read_pickle('Pickle2.pkl')
test_set=['Pickle1.pkl','Pickle2.pkl']
train_sets=['Unpolarized_dataset.pkl']
faltudf=pd.read_pickle('Pickle1.pkl')
# testing models on one another
models=['LinearSVC'	,'MultinomialNB','LogisticRegression','SGDClassifier']
for train in train_sets:
	
	df1=pd.read_pickle(train)
	df1=pd.concat([faltudf,df1])
	print(len(df1))
	df1.drop_duplicates(subset=['created_utc'],keep=False,inplace=True) 
	print(len(df1))
	for test in test_set:
		df2=pd.read_pickle(test)
		print("----Dataset Used :"+test+"-------")
		df1['title']=df1['title']+df1['selftext']
		df2['title']=df2['title']+df2['selftext']


		X_train=[str(i)+" " for i in df1['title'].values]
		y_train=df1.link_flair_text.values
		X_test=[str(i)+" " for i in df2['title'].values[:100]]
		y_test=df2.link_flair_text.values[:100]
		vectorizer = TfidfVectorizer()
		X_train = vectorizer.fit_transform(X_train)
		X_test = vectorizer.transform(X_test)


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
		# predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))
		# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
		clf=LogisticRegression()
		clf.fit(X_train,y_train)
		# predicted=clf.predict(X_test)
		print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)))


