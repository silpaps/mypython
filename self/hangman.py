import random
from words import words
import string
def get_valid_word(words):
    word=random.choice(words) #randomly chosess something from the list
    while '-' in word or '' in word:
        word=random.choice(words)

    return word
def hangman():
    word=get_valid_word(words)
    word_letters=set(word)

