import spacy
nlp = spacy.load('en_core_web_sm')

from spacy import displacy

doc = nlp("Over the last quarter, Apple sold nearly twenty thousand iPods for a profit of $6 million." "By contrast, Sony only sold 8000 Walkman music players.")
#doc = displacy.render(doc, style = 'ent', jupyter = True)

for sentence in doc.sents:
    displacy.render(sentence, jupyter = True, style = 'ent')

options = {'ents': ['PRODUCT', 'ORG']}
displacy.render(doc, style = 'ent', jupyter = True, options = options, )

colors = {'ORG': 'red', 'PRODUCT': 'blue'}
options = {'ents': ['PRODUCT', 'ORG'], 'colors': colors}
displacy.render(doc, style = 'ent', jupyter = True, options = options)

colors = {'ORG': 'radial-gradient(yellow, green)' }
options = {'ents': ['PRODUCT', 'ORG'], 'colors': colors}
displacy.render(doc, style = 'ent', jupyter = True, options = options)

colors = {'ORG': 'linear-gradient(green, yellow)' }
options = {'ents': ['PRODUCT', 'ORG'], 'colors': colors}
displacy.render(doc, style = 'ent', jupyter = True, options = options)

displacy.serve(doc, style = 'ent', options = options)
