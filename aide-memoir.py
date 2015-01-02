#!/usr/bin/env python3

import random

dictionary = dict()

with open("dictionary.txt") as dictionary_file:
    for line in dictionary_file:
        (english, french) = line.split(":")
        dictionary[english] = french.strip()

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
