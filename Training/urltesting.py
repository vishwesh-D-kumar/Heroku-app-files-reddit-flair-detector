#A command line interface to input url and predict flair
import pandas as pd
# import pickle
import praw
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from  sklearn.metrics  import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
warnings.filterwarnings("ignore")

reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')


pkl='Unpolarized_dataset.pkl'
df=pd.read_pickle(pkl)
# df2=pd.read_pickle('Pickle1.pkl')
# df=pd.concat([df1,df2])
# print(len(df))
# df.drop_duplicates(subset=['created_utc'],keep='first',inplace=True) 
# print(len(df))
df['title']=df['title']+df['selftext']
X_train=[str(i)+" " for i in df['title'].values]
y_train=df.link_flair_text.values
url=input()
sub=reddit.submission(url=url)
y_test=[sub.link_flair_text]
# r=clf.predict(vectorizer.transform([sub.title+" "+sub.selftext]))
vectorizer = TfidfVectorizer()
X_test=[sub.title+" "+sub.selftext]
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
# pickle.dump(vectorizer, open("TrainedModels/Unpolarized_dataset/vectorizer_final", 'wb'))
clf=LinearSVC()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)),predicted,y_test)
# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
# try:
clf=MultinomialNB()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)),predicted,y_test)
# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
# except:
# 	print("MultinomialNB left , attribute is negative")
clf=SGDClassifier()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)),predicted,y_test)
# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
clf=RandomForestClassifier()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)),predicted,y_test)
# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))
clf=LogisticRegression()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
print(type(clf).__name__+" "+str(accuracy_score(y_test,predicted)),predicted,y_test)
# pickle.dump(clf, open("TrainedModels/Unpolarized_dataset/"+type(clf).__name__, 'wb'))


