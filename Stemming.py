import spacy
nlp = spacy.load('en_core_web_sm')

import nltk
from nltk.stem.porter import PorterStemmer

p_stemmer = PorterStemmer()

words = ['run', 'ran', 'runner', 'runs', 'easily', 'fairly', 'fairness']

for word in words:
    print(word + ' ----> ' + p_stemmer.stem(word))
    
from nltk.stem.snowball import SnowballStemmer
s_stemmer = SnowballStemmer(language = 'english')
for word in words:
    print(word + ' ----> ' + s_stemmer.stem(word))
