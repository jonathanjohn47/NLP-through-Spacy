import pandas as pd
import numpy as np

df = pd.read_csv("spam.csv", sep = ',', encoding='latin-1')
df = df.iloc[:, [0,1]]
df.isnull().sum()


df['v1'].value_counts()

#-------------------------------------------------------------
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #This is a redundant step. No use in actual vectorization and classification
l = []
p = []
for i in df['v2']:
    count = 0
    l.append(len(i))
    for j in punctuations:
        if j in i:
            count = count + 1
    p.append(count)
df['length'] = l
df['punctuation'] = p
df
#-------------------------------------------------------------

from sklearn.model_selection import train_test_split
X = df['v2']
y = df['v1']
X_train, X_test, y_train, y_test = train_test_split(X,y)

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
text_clf.fit(X_train, y_train)

predictions = text_clf.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
cm = confusion_matrix(predictions, y_test)
cm = pd.DataFrame(cm)
cm.columns = ['Ham', 'Spam']
cm.index = ['Ham', 'Spam']
cm

print(text_clf.predict(["Congratulations! You have won 3 tickets to Australia. text AUS to 5252."]))
