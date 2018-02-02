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
word_bank = ["a step ahead of cataclysm", "metal is perfection", "i feel your fear", "looks can be deceiving",
             "consume and adapt", "unmatched power", "imagine if i had a real weapon", "we are as one",
             "trample their bones", "no pain no drain"]
guesses = 11
alphabet = list(string.ascii_lowercase)
random_word = random.choice(word_bank)
correct = list(random_word)
print("Choose a letter. These are quotes from League of Legends. You ten tries")
letters_guessed = []


while guesses > 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    guesses -= 1
    print(guesses)
    join = " ".join(output)
    print(join)
    if output == correct:
        print("You Win Good Job XD!")
        exit(0)
    print("These are your letters you can guess :), %s" % alphabet)
    ask_for_letter = input("Name a letter")
    lowercase_guess = ask_for_letter.lower()
    letters_guessed.append(lowercase_guess)
    if lowercase_guess in alphabet:
        alphabet.remove(lowercase_guess)
    if guesses == 0:
        print("You Lose The Word Was %s" % random_word)