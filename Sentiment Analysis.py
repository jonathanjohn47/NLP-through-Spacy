import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

a = "This is a good movie"
sid.polarity_scores(a)

import pandas as pd
data = pd.read_csv("Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv")
X = data['reviews.text'].values
X = pd.DataFrame(X)
X.columns = ["Reviews"]
data
#X.isnull().sum()
#X.dropna(inplace=True)

polarity = []
for review in X["Reviews"]:
    polarity.append(sid.polarity_scores(review).get("compound"))

sentiment = []
for i in polarity:
    if i>0:
        sentiment.append("Positive")
    elif i==0:
        sentiment.append("Neutral")
    else:
        sentiment.append("Negative")
X["Sentiment"] = sentiment
X
