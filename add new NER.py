from spacy.tokens import Span
ORG = doc.vocab.strings[u"ORG"]

new_ent = Span(doc,0,1,label=ORG)
doc.ents = list(doc.ents) + [new_ent]
