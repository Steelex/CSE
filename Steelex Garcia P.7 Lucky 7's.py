import random
# Steelex Garcia
# Period 3

print()
broke = False
money = 15
played = 0
high = 0
while money > 0 and broke is False:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You rolled a", total)
    if total == 7:
        money += 4
        played += 1
    else:
        money -= 1
        played += 1
    if high < money:
        high = money
        numb = played
    if money == 0:
        broke = True
        print("Rounds played", played)
        print("Highest money is %s on round %s" % (high, numb))
