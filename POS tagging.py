import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'A quick brown fox jumped over the lazy dog\'s back')
print(doc.text)

print(doc[4].pos_)
print(doc[4].tag_)

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

doc = nlp(u"I read books on NLP.")
word = doc[1]
token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

doc = nlp(u"Last night I read a book on NLP.")
word = doc[3]
token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

doc = nlp(u'A quick brown fox jumped over the lazy dog\'s back')

POS_counts = doc.count_by(spacy.attrs.POS)

for k,v in sorted(POS_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")

TAG_counts = doc.count_by(spacy.attrs.TAG)

for k,v in sorted(TAG_counts.items()):
    print(f"{k:{20}}  {doc.vocab[k].text:{5}} {v}")
