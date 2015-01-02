#!/usr/bin/env python3

import random

dictionary = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "swimming pool": "piscine"
}

while True:
    english_word = random.choice(list(dictionary.keys()))
    print("English: " + english_word)
    french_guess = input("French? ")
    french_word = dictionary[english_word]
    if french_guess == french_word:
        print("Correct!")
    else:
        print("Wrong; it's actually: " + french_word)
    print("")
