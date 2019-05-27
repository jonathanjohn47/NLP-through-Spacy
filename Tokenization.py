import spacy
nlp = spacy.load('en_core_web_sm')
mystring = "Some string"
doc = nlp(mystring)

for token in doc:
  print(token.text, token.pos_, token.dep_)
