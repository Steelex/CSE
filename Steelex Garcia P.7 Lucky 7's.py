import random
# Steelex Garcia
# Period 7

print()
broke = False
money = 15
played = 0
high = 0
while money > 0 and broke is False :
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You rolled a", total)
    played += 1
    if total == 7:
        money += 4
    else:
        money -= 1
    if high < money:
        high = money
        thing = round
    if money == 0:
        broke = True
        print("Rounds played", played)
