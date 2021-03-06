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

#Adding a phrase as a new entity
doc = nlp("Our company created a brand new vacuum cleaner." "This new vacuum-cleaner is the best in show")
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

phrase_list = ['vacuum cleaner', 'vacuum-cleaner']

phrase_patterns = [nlp(text) for text in phrase_list]

matcher.add('newproduct', None, *phrase_patterns)

found_matches = matcher(doc)
found_matches

from spacy.tokens import Span
PROD = doc.vocab.strings['PRODUCT']

new_ents = [Span(doc, match[1], match[2], label=PROD) for match in found_matches]
doc.ents = list(doc.ents) + new_ents

show_ents(doc)

#finding how many times a named entity is present in the document
doc = nlp("Originally I paid $29.95 for this car toy, but now it is marked down by 10 dollars.")
[ent for ent in doc.ents if ent.label_ == 'MONEY']
