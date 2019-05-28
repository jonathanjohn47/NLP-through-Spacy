from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

import os
path = os.getcwd()
with open(path + '\\reaganomics.txt') as f:
    doc3 = nlp(f.read())

phrase_list = ['voodoo economics', 'supply-side eoconomics', 'trickle-down economics', 'free-market economics']

phrase_patterns = [nlp(text) for text in phrase_list]

'''for pattern in phrase_patterns:
    matcher.add('EconMatcher', None, pattern)
'''
matcher.add('EconMatcher', None, *phrase_patterns)

found_matches = matcher(doc3)
found_matches

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc3[start-5:end+5]
    print(match_id, string_id, start, end, span.text)
