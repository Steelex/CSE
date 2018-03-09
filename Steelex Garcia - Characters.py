class Character(object):
    def __init__(self, name, description, health, move):
        self.name = name
        self.interact = False
        self.alive = True
        self.description = description
        self.attack = False
        self.take_damage = False
        self.health = health
        self.move = move

    def interaction(self):
        self.interact = True
        print(self.name)
        print(self.description)
        print(self.health)
        self.interact = False

    def hit(self):
        self.take_damage = True
        self.health = self.health - 1
        print("You damaged the enemy and now the enemy has lost health.")
        print(self.health)
        if self.health == 0:
            print("The enemy dies and fades away.")
            self.alive = False
        elif self.health < 0:
            print("You have taken down your enemy.")

    def movement(self):
        self.move = True
        print("The enemy is moving")
        self.move = False


monster = Character("Energy Sentinal", "A big, blue, energy sentinal.", 5, False)
monster.interaction()
monster.movement()
monster.hit()
monster.hit()
monster.hit()
monster.hit()
monster.hit()