import random
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
correct_phrase = False
lives = 10
start = True
letters_guessed = [""]
while lives > 0 and correct_phrase is False:
        random.shuffle(word_bank)
        word = word_bank.pop(7)
        word = (list(word))
        print(word)
