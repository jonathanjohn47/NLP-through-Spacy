import pandas as pd
import random

data1 = pd.read_csv("news_summary.csv", encoding="latin-1")
data2 = pd.read_csv("news_summary_more.csv", encoding="latin-1")

data1 = pd.DataFrame(data1['text'])
data2 = pd.DataFrame(data2['text'])
data = pd.concat([data1, data2], axis=0)
data = data.iloc[random.randint(0,len(data['text']))]
data

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words='english')
dtm = cv.fit_transform(data)
dtm

from sklearn.decomposition import LatentDirichletAllocation
LDA = LatentDirichletAllocation(n_components=50, random_state=42)

LDA.fit(dtm)

#Grab the vocabulary of words
cv.get_feature_names()

#Grab the topics
LDA.components_.shape

single_topic = LDA.components_[random.randint(0,len(LDA.components_))]
top_ten_words = single_topic.argsort()[-20:] #Shows us index of elements arranged in ascending order
top_ten_words

for index in top_ten_words:
    print(cv.get_feature_names()[index])
