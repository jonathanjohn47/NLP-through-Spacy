import spacy
nlp = spacy.load('en_core_web_sm')

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(f"{ent.text:{30}}  -   {ent.label_:{10}}   -   {str(spacy.explain(ent.label_))}")
    else:
        print('No entities found')

doc = nlp('Hi!How are you?')
show_ents(doc)

doc = nlp("May I go to Washington DC next May to see the Washington Monument?")
show_ents(doc)

doc = nlp("Can I please have 500 dollars of Microsoft stock?")
show_ents(doc)

doc = nlp("Tesla to build a U.K. factory for $6 million")
show_ents(doc)

#Add new entity 
from spacy.tokens import Span
ORG = doc.vocab.strings[u"ORG"]

new_ent = Span(doc,0,1,label=ORG)
doc.ents = list(doc.ents) + [new_ent]

show_ents(doc)
