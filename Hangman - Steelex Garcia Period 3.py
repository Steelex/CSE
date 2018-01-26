import random
import string
# Steelex Garcia
# Period 3
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random word from the item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
word_bank = ["A step ahead of cataclysm", "Metal is perfection", "I feel your fear", "Looks can be deceiving",
             "Consume and adapt", "Unmatched Power", "Imagine if I had a real weapon", "We are as one",
             "Trample their bones", "No pain no drain"]
lives = 10
word = (random.choice(word_bank))
word = (list(word))
length = len(output)
print(word)
letters = ["abcdefghijklmnopqrstuvwxyz"]
words_guessed = []
while lives > 0:
    guess = input("Guess a letter or try the whole word. ")
    if guess == word:
        print("Good Job You Did It!")
    if guess == word:
        print("Good Job")
    if guess != word:
        lives -= 1
        print("You have %s guesses left" % lives)

