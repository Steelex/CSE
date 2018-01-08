import random
# Steelex Garcia
# Period 7


print()
# print(number)   to know what the number is
# Describes exactly ONE turn. The while is the Game Controller.
number = (random.randint(1, 50))
print("I am thinking of a number between 1 and 50.")
guess = 0
guess_made = 0
while int(guess) != number and guess_made < 5:
    guess = input("What number am I thinking of?")
    if (int(guess)) == number:
        print("You got it! Good Job!")
    elif int(guess) > number:
        print("Go Lower.")
        guess_made += 1
    elif int(guess) < number:
        print("Go Higher")
        guess_made += 1
    if guess_made >= 5:
        print("You ran out of tries. Better Luck next time.")
