import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp(u"A quick brown fox jumps over the lazy dog's back")

options = {'distance': 110, 'compact': False, 'color':'blue', 'font': 'Calibri'}

from spacy import displacy

displacy.render(doc,style = 'dep', jupyter = True, options = options)

doc2 = nlp("This is a sentence. This is another sentence. This is third sentence possibly longer than the other two.")

spans = list(doc2.sents)

displacy.serve(spans,style = 'dep', options = options)
