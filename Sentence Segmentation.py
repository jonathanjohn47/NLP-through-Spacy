import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("This is a sentence. This is a second sentence. This is a third sentence probably greater than the other two.")

for sents in doc.sents:
    print(sents)

#doc.sents[0]
listdoc = list(doc.sents)
listdoc[0]

doc = nlp(u'"Management is doing the right things; leadership is doing the right things"- Peter Drucker')

for sent in doc.sents:
    print(sent)
    print('\n')

#Add a segmentation rule
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ";":
            doc[token.i+1].is_sent_start = True
        if token.text == "\"":
            doc[token.i+1].is_sent_start = False
    return doc       

nlp.add_pipe(set_custom_boundaries, before = 'parser')
nlp.pipe_names

doc2 = nlp(u'"Management is doing the right things; leadership is doing the right things"- Peter Drucker')
for sent in doc2.sents:
    print(sent)

#Change segmentation rule
mystring = "This is a sentence. This is another sentence. \n\n This is \nthe third sentence."
doc = nlp(mystring)

for sent in doc.sents:
    print(sent)
    print('-')

from spacy.pipeline import SentenceSegmenter

def split_on_newlines(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True
    yield doc[start:]
            

sbd = SentenceSegmenter(nlp.vocab, strategy = split_on_newlines)
nlp.add_pipe(sbd)

doc = nlp(mystring)
for sent in doc.sents:
    print(sent)
