doc = nlp(u'A quick brown fox jumped over the lazy dog\'s back')

POS_counts = doc.count_by(spacy.attrs.POS)
for k,v in sorted(POS_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")

TAG_counts = doc.count_by(spacy.attrs.TAG)
for k,v in sorted(TAG_counts.items()):
    print(f"{k:{20}}  {doc.vocab[k].text:{5}} {v}")
