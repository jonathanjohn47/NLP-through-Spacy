import spacy
nlp = spacy.load('en_core_web_sm')
mystring = "Some string"
doc = nlp(mystring)

for token in doc:
  print(token.text, token.pos_, token.dep_)

for entity in doc.ents:
  print(entity, entity.label_)
  print(str(spacy.explain(entity.label_)))
  print('\n')
  
from spacy import displacy
displacy.render(doc, style = 'dep', jupyter = True)
displacy.render(doc, style = 'ent', jupyter = True)
