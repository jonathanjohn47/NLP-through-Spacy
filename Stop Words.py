import spacy
nlp = spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))
print(nlp.vocab['the'].is_stop)
print(nlp.vocab['mystery'].is_stop)

nlp.Defaults.stop_words.add('btw')
nlp.vocab['btw'].is_stop = True

print(nlp.vocab['btw'].is_stop)

nlp.Defaults.stop_words.remove('btw')
nlp.vocab['btw'].is_stop = False

print(nlp.vocab['btw'].is_stop)
print(len(nlp.Defaults.stop_words))
