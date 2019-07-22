from django.shortcuts import render
import praw
import pickle
# import pandas as pd
# import pandas as pd
# import nltk 
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from nltk.corpus import stopwords
# from ast import literal_eval
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from  sklearn.metrics  import accuracy_score
# from sklearn.linear_model import SGDClassifier
# from sklearn.svm import LinearSVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split

models=['LinearSVC'	,'MultinomialNB',
'LogisticRegression','SGDClassifier','RandomForestClassifier']


# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'flairpredict/home.html', context=None)
def results(request):
	redditlink=request.POST['redditlink']
	# try:
	
	data=predictor(redditlink)
	flairs=data[0]
	actual_flair=data[-1]
	return render(request, 'flairpredict/results.html', context={'flairs':flairs,'actual_flair':actual_flair})
	# except:
	# 	return HttpResponse("Not a Valid")

def analysis(request):

	type=request.GET.get('type')
	if type=='misc':
		return render(request, 'flairpredict/misc.html', context=None)
	if type=='time':
		flair=request.GET.get('flair')
		return render(request, 'flairpredict/time.html', context={'allowed_flairs':['AMA','Science and Technology','Food', 'Photography', 'Policy and Economy','[R]eddiquette','r and all','Non-Political','Sports','AskIndia','Politics'],'flair':flair})
	if type=='sentiment':
		return render(request, 'flairpredict/sentiments.html', context=None)
	
	flair=request.GET.get('flair')
	if flair=='None':
		return render(request, 'flairpredict/analysis.html', context={'allowed_flairs':['AMA','Science and Technology','Food', 'Photography', 'Policy and Economy','[R]eddiquette','Non-Political','Sports','AskIndia','Politics'],'flair':flair})
	if flair=='Science/Technology':
		flair='Science and Technology'
	if flair=='r/all':
		flair='r.all'
	return render(request, 'flairpredict/analysis.html', context={'allowed_flairs':['AMA','Science and Technology','Food', 'Photography', 'Policy and Economy','[R]eddiquette','Non-Political','Sports','AskIndia','Politics'],'flair':flair})



	# return HttpResponse(redditlink)
def retrieve_data():
	clfs=[]
	for model in models:
		clf = pickle.load(open('flairpredict/static/flairpredict/TrainedModels/Final_models/'+model, 'rb'))
		clfs.append(clf)
	vectorizer=pickle.load(open('flairpredict/static/flairpredict/TrainedModels/Final_models/vectorizer_final','rb'))
	return clfs,vectorizer

def predictor(redditlink):
	x=retrieve_data()
	clfs=x[0]
	vectorizer=x[1]
	
	sub=submission(redditlink)
	predicted=[]
	for clf in clfs:
		r=clf.predict(vectorizer.transform([sub.title+" "+sub.selftext]))[0]
		predicted.append(r)
	flairs={}
	c=0
	for model in models:
		flairs[model]=predicted[c]
		c+=1

	return flairs,sub.link_flair_text

def submission(redditlink):
	reddit = praw.Reddit(client_id='wV2C1cRllfQD2A', \
                     client_secret='56yVXFTW9ZlAFFrXo4NN-exb2EY', \
                     user_agent='PrawTrial', \
                     username='vishweshDkumar', \
                     password='bakabaka')
	return reddit.submission(url=redditlink)









