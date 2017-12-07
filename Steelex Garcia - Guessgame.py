import random
# Steelex Garcia

print()
# print(number)   to know what the number is

number = (random.randint(1, 50))
print("I am thinking of a number between 1 and 50.")
guess = 5
guess_made = 0
while int(guess) != number:
    guess = input("What number am I thinking of?")
    if (int(guess)) == number:
        print("You got it! Good Job!")
    elif int(guess) > number:
        print("Go Lower.")
        guess_made += 1
    elif int(guess) < number:
        print("Go Higher")
        guess_made += 1
if guess_made > 5:
    print("You ran out of tries. Better Luck next time.")
