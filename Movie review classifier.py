import numpy as np
import pandas as pd

data = pd.read_csv("movie_review.csv")
print(data.isnull().sum())
data.dropna(inplace = True)

X = data.iloc[:,-2].values
y = data.iloc[:,-1].values
y = ["Positive review" if i=='pos' else "Negative review" for i in y]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y)

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
text_clf.fit(X_train, y_train)

predictions = text_clf.predict(X_test)
predictions

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
cm = confusion_matrix(predictions, y_test)
cm = pd.DataFrame(cm)
cm.columns = ['Positive', 'Negative']
cm.index = ['Positive', 'Negative']
cm

print(text_clf.predict(["<<Movie Review>>"]))
