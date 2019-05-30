from spacy.tokens import Span
ORG = doc.vocab.strings[u"ORG"]

new_ent = Span(doc,0,1,label=ORG) # 0 is the starting token in span of doc, 1 is the ending token (exclusive) in span of the doc.
doc.ents = list(doc.ents) + [new_ent]
