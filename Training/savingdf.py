###Code to save data to mongodb instance
collections=['new_subs','top_subs','unpolarized']
import pandas as pd
import pymongo
from pymongo import MongoClient
df=pd.read_pickle('Unpolarized_dataset.pkl')
client=MongoClient()
db = client.rIndiadata
collection = db.unpolarized
df.index=['sub'+str(i) for i in range(len(df))]
# collection.insert_one(df.to_dict())
###Retrieving data : run to retrieve data with collection set asone of the collections from the above list [collections]
df2=pd.DataFrame.from_dict(collection.find_one())
print(df2)