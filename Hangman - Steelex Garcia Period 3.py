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
alphabet = list(string.ascii_lowercase)
random_word = random.choice(word_bank)
correct = list(random_word)
print("This is Hangman. Each of my guesses are phrases are from LOL. Can you guess them? You have 10 tries.")
letters_guessed = []
tries = 10
while tries > 0:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    tries -= 1
    if output == correct:
        print("You Win Good Job XD!")
        exit(0)
    print("You can guess these letters:), %s" % alphabet)
    ask_for_letter = input("Guess a letter or even the whole word.")
    lowercase_guess = ask_for_letter.lower()
    letters_guessed.append(lowercase_guess)
    if lowercase_guess in alphabet:
        alphabet.remove(lowercase_guess)
    if tries == 0:
        print("Game Over. The words are %s" % random_word)
