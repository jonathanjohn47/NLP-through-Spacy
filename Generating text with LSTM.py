def read_file(path):
    with open(path) as f:
        str_text = f.read()
        
    return str_text

def separate_punc(text):
    #return [token.text.lower() for token in nlp(text) if token.text not in '\n\n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n']
    token_text = []
    for token in nlp(text):
        if token.text not in '\n\n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n':
            token_text.append(token.text.lower())
    return token_text

import numpy as np
import pandas as pd

import spacy
nlp = spacy.load('en', disable = ['parser', 'tagger', 'nen'])
nlp.max_length = 1198623

data = read_file("moby_dick.txt")
tokens = separate_punc(data)

#pass in 25 words, and Neural Network predict the 26th word.

train_length = 25+1
text_sequences = []

for i in range(train_length, len(tokens)):
    text_sequences.append(tokens[i-train_length:i])

#check what the sequences are:
print(' '.join(text_sequences[0]))
print("\n")
print(' '.join(text_sequences[1]))
print("\n")
print(' '.join(text_sequences[2]))

#Each sequence is one token ahead of the previous one

#tokenize into keras tokenizer
from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_sequences)

print(tokenizer.word_counts)

sequences = tokenizer.texts_to_sequences(text_sequences)
sequences = np.array(sequences)
sequences

from keras.utils import to_categorical
X = sequences[:,:-1]
y = sequences[:,-1]
vocabulary_size = len(tokenizer.word_counts)
y = to_categorical(y, num_classes=vocabulary_size+1)
seq_len = X.shape[1]

from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding

def modelcreate(vocabulary_size, seq_len):
    model = Sequential()
    model.add(Embedding(vocabulary_size, seq_len, input_length = seq_len))
    model.add(LSTM(50, return_sequences = True))
    model.add(LSTM(50))
    model.add(Dense(50, activation = 'relu'))
    model.add(Dense(vocabulary_size, activation="softmax"))
    
    model.compile(loss = 'categorical_crossentropy', optimizer = 'Adam', metrics = ['accuracy'])
    model.summary()
    
    return model

model = modelcreate(vocabulary_size+1, seq_len)

from pickle import dump,load
model.fit(X,y,batch_size = 128, epochs = 1000, verbose = 1)

model.save('my_mobidickmode.h5')
dump(tokenizer, open('my_simple_tokenizer','wb'))

from keras.preprocessing.sequence import pad_sequences
def gen_text(model, tokenizer, seq_len, seed_text, num_words_to_generate):
    output_text = []
    input_text = seed_text
    for i in range(num_words_to_generate):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')
        pred_word_index = model.predict_classes(pad_encoded, verbose = 0)[0]
        predicted_word = tokenizer.index_word[pred_word_index]
        input_text = input_text + ' ' + predicted_word
        output_text.append(predicted_word)
    
    return ' '.join(output_text)

import random
random_text = text_sequences[random.randint(0,len(text_sequences))]
seed_text = ' '.join(random_text)

print(gen_text(model, tokenizer, seq_len, seed_text=seed_text, num_words_to_generate=25))

