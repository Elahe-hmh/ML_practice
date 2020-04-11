# -*- coding: utf-8 -*-
"""Tokenization&padding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ti8wAQ3Y00o0WBho0VVefn8j4S0YWLdR
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences=[
           'I love my dog',
           'I love my cat',
           'you love my dog!',
           'Do you think my dog is amazing?'
]

tokenizer=Tokenizer(num_words=100,oov_token="<00V>")
tokenizer.fit_on_texts(sentences)
word_index=tokenizer.word_index

sequences=tokenizer.texts_to_sequences(sentences)

padded=pad_sequences(sequences)

print(word_index)
print(sequences)
print(padded)

test_data=[
           'I really love my dog because is so cute!',
           'my dog loves my manatee'
]

sequences_test=tokenizer.texts_to_sequences(test_data)

padded_test=pad_sequences(sequences_test)
print(word_index)
print(sequences_test)
print(padded_test)
#0 is for padding, 1 is for oov

"""padding has a parameter for where we want zeros to be! before or after sentences. for after write this:***` padding='post'`*** after sequences argument

`***maxlen=5***` is for times that you don`t want padding as long as your longest sentence.

but what if some of our sentences are longer than maxlen?? use **`truncating='post`**
"""