#Reddit Flair Detector
This is a Flair detector working on the following flairs in r/India
###Vishwesh Kumar: vishwesh18119@iiitd.ac.in
##USED FLAIRS: IMPORTANT: the used flairs are :['AMA','Science/Technology','Food','Demonetization', 'Photography', 'Policy & Economy','[R]eddiquette','r/all','Non-Political','Sports','AskIndia','Politics']


##Directory Structure:
There Directory is split into Two Directories:

Training                                                                 | Heroku-app
------------------------------------------------------------------------ | ---------------------
Contains data required for training and selecting model before deploying | App deployed on heroku

##Training
*All .py files have details inside them : here is a idea of major files they do :
	* urltesting.py : A command line interface to input url and predict flair
	*process_data.py : Checking Database accuracy on one another to pick best accuracy
	*process_comments.py: Used to train models on textual data
	*pushshift.py and unpolarized_data.py:Scraping data off of reddit
	*savingdf.py: Contains command to run to store and retrieve currently saved databases
*Results folder:Contains Results of dataset training on Models by attributes used
*Models Used for Training :['LinearSVC'	,'MultinomialNB','LogisticRegression','SGDClassifier','RandomForestClassifier']
	*Final Features used after testing for accuracy: Title text and Self text: 68 % accuracy (78% best accuracy on Pickle2.pkl database)
	*Used Combined datasets of pickle2 and Unpolarized_dataset.pkl to make final model
	*Best accuracy by LinearSVC 
*Scraped Data: saved in three pickle files : which are saved as dictionary pandas dataframes on mongodb along with being stored locally for convienience:
	*Pickle1.pkl: The newest approx 900 posts
	*Pickle2.pkl: The top approx 900 posts
	*Unpolarized_dataset.pkl:Contains a 100 submissions sorted by relevance for each allowed flair
*Used the praw api along with pushshift api to collect posts(pushshift sometimes gave incosistent results in case of the flair attribute of the submissions)*

##Deployed : heroku app: deployed on website: https://redditflairpredictor.herokuapp.com/flairpredict/


##Approach: 
*Initially scraped attributes:['created_utc','score','selftext','is_video',"title",
'over_18','num_comments','is_reddit_media_domain','num_crossposts','is_self','link_flair_text','comment_text','net_comment_score'] 
*Tested data on all three datasets available on each attribute:
picked best accuracy datasets and attributes together to test them 
*Used Vectorizer module to for text to vectors
*Used nltk library to preprocess textual data*

##Running the app

*All requirements to run Heroku-app can be found inside Heroku-app/Reddit/requirements.txt
*after doing so go to directory by running these commands after cloning the repository*

```bash
cd Heroku-app/Reddit/
python manage.py runserver
```
##Refrences used : 
Can be found inside Training/Helpful Links with descriptions







