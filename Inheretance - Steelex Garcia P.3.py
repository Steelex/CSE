""""
class Vehicle(object):
    def __init__(self, seats, engine_type, turning_mechanism):
        self.seats = seats
        self.engine_type = engine_type
        self.turning_mechanism = turning_mechanism

    def move(self):
        print("You move forward")

    def change_direction(self):
        print("You change direction")


class Car(Vehicle):
    def __init__(self, seats, horsepower):
        super(Car, self).__init__(seats, 'engine', 'steering wheel')
        self.hp = horsepower

    def turn_on(self):
        print("You turn the key and the engine starts")


test_car = Car(4, 9001)
test_car.turn_on()
test_car.change_direction()
print(test_car.turning_mechanism)


class KeylessCar(Car):
    def __init__(self, seats, hp):
        super(KeylessCar, self).__init__(seats, hp)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeylessCar(4, 9002)
cool_car.turn_on()

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)
"""""



class Character(object):
    def __init__(self, name, description, health, move, attack, defense):
        self.name = name
        self.alive = True
        self.description = description
        self.attack = False
        self.take_damage = False
        self.health = health
        self.movement = move
        self.attack = attack
        self.defense = defense

    def interact(self):
        print(self.name)
        print(self.description)
        print(self.health)

    def hit(self):
        self.take_damage = True
        self.health = self.health - 1
        print("You hit the enemy.")
        print(self.health)
        if self.health == 0:
            print("The enemy dies.")
            self.alive = False
        elif self.health < 0:
            print("Your enemy is dead.")
        self.take_damage = False

    def take_hit(self):
        self.take_damage = True
        self.health = self.health - 1
        print("You take damage.")
        if self.health == 0:
            print("You have died. GAME OVER.")
            quit()

    def move(self):
        self.movement = True
        print("The enemy moves!")
        self.movement = False

    def status(self):
        print("%s/5 health left" % self.health)


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage, ability, attack_type):
        super(Weapon, self).__init__(name, description)
        self.damage = damage
        self.ability = ability
        self.attack_type = attack_type


class Armor(Item):
    def __init__(self, name, description, ability, defense_type, hp):
        super(Armor, self).__init__(name, description)
        self.ability = ability
        self.defense_type = defense_type
        self.hp = hp


class Heavy_Armor(Armor):
    def __init__(self, name, hp, defense_type, ability, description):
        super(Heavy_Armor, self).__init__(name, description, ability, defense_type, hp)
        self.hp = hp
        self.defense_type = defense_type
        self.ability = ability

class Light_Armor(Armor):
    def __init__(self, name, hp, speed, defense_type, ability, description):
        super(Light_Armor, self).__init__(name, description, ability, defense_type, hp)
        self.hp = hp
        self.speed = speed
        self.defense_type = defense_type
        self.ability = ability


class Dangerous_Armblades(Weapon):
    def __init__(self, name, damage, ability, attack_type, description):
        super(Dangerous_Armblades, self).__init__(name, description, damage, ability, attack_type)
        self.damage = damage
        self.ability = ability
        self.attack_type = attack_type

class Health_Hammer(Weapon):
    def __init__(self, name, damage, ability, hp, attack_type, description):
        super(Health_Hammer,self).__init__(name, description, damage, ability, attack_type)
        self.damage = damage
        self.hp = hp
        self.ability = ability
        self.attack_type = attack_type

class Speed_Rapier(Weapon):
    def __init__(self, name, damage, ability, speed, attack_type, description):
        super(Speed_Rapier, self).__init__(name, description, damage, ability, attack_type)
        self.damage = damage
        self.ability = ability
        self.speed = speed
        self.attack_type = attack_type

class Consumable(Item):
    def __init__(self, name, description):
            super(Consumable, self).__init__(name, description)
            self.use = False
            self.amount = 0

    def obtain(self):
            self.amount = self.amount + 1
            print("You have obtained a %s" % self.name)


class Lesser_Health_Potion(Consumable):
    def __init__(self):
        super(Lesser_Health_Potion, self).__init__("Weaker Healing Potion", "A potion the will restore 3 HP.")

    def use(self):
        self.use = True
        self.health = self.health + 3
        self.amount = self.amount - 1
        print("You have used a lesser health potion.")
        self.use = False


class Health_Potion(Consumable):
    def __init__(self):
            super(Health_Potion, self).__init__("Regular Healing Potion", "A potion the will restore 5 HP.")

    def use(self):
        self.use = True
        self.health = self.health + 5
        self.amount = self.amount - 1
        print("You have used a regular health potion.")
        self.use = False

class Greater_Health_Potion(Consumable):
    def __init__(self):
        super(Greater_Health_Potion, self).__init__("Greater Healing Potion", "A potion the will restore 10 HP.")

    def use(self):
        self.use = True
        self.health = self.health + 10
        self.amount = self.amount - 1
        print("You have used a greater health potion.")
        self.use = False


class Greater_Mana_Potion(Consumable):
    def __init__(self):
        super(Greater_Mana_Potion, self).__init__("Greater Mana Potion", "A potion the will restore 10 Mana.")

    def use(self):
        self.use = True
        self.mana = self.mana + 10
        self.amount = self.amount - 1
        print("You have used a greater mana potion.")
        self.use = False


class Regular_Mana_Potion(Consumable):
    def __init__(self):
        super(Regular_Mana_Potion, self).__init__("Regualr Mana Potion", "A potion the will restore 5 Mana.")

    def use(self):
        self.use = True
        self.mana = self.mana + 5
        self.amount = self.amount - 1
        print("You have used a regular mana potion.")
        self.use = False


class Lesser_Mana_Potion(Consumable):
    def __init__(self):
        super(Lesser_Mana_Potion, self).__init__("Lesser Mana Potion", "A potion the will restore 3 Mana.")

    def use(self):
        self.use = True
        self.mana = self.mana + 3
        self.amount = self.amount - 1
        print("You have used a lesser mana potion.")
        self.use = False


class Relic(Item):
    def __init__(self, name, description, ability):
        super(Relic, self).__init__(name, description)
        self.ability = ability


class Offense_Booster(Relic):
    def __init__(self, name, description, ability, damage):
        super(Offense_Booster, self).__init__(name, description, ability)
        self.ability = ability
        self.damage = damage


class Health_Booster(Relic):
    def __init__(self, name, description, hp, ability):
        super(Health_Booster, self).__init__(name, description, ability)
        self.ability = ability
        self.hp = hp


class Speed_Booster(Relic):
    def __init__(self, name, description, ability, speed):
        super(Speed_Booster, self).__init__(name, description, ability)
        self.ability = ability
        self.speed = speed


