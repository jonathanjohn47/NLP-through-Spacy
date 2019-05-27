import spacy
nlp = spacy.load("en_core_web_sm")

string = "some string"
doc = nlp(string)

import numpy as np
import pandas as pd

t = []
for token in doc:
    if token.text in t:
        pass
    else:
        t.append(token.text)
        t.append(token.pos_)
        t.append(token.lemma)
        t.append(token.lemma_)

t = np.array(t)
t = t.reshape(-1,4)
t = pd.DataFrame(t)
t.columns = ["Text", "Part of Speech", "Lemma Hash", "Lemma"]
print(t)
