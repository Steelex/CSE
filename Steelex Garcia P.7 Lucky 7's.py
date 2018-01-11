import random
# Steelex Garcia
# Period 7

print()

money = 15
played = 0

while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You rolled a", total)
    played += 1
    if total == 7:
        money += 4
    else:
        money -= 1
print("Rounds played", played)
