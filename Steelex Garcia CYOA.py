class Room(object):
    def __init__(self, name, north, west, east, south, se, sw, ne, nw, description, enemy_in):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.southeast = se
        self.southwest = sw
        self.northeast = ne
        self.northwest = nw
        self.description = description
        self.enemy_in = enemy_in

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

class Character(object):
    def __init__(self, name, health, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.money = money
        self.inventory = inventory
        self.alive = True

    def take_damage(self, amount):
        self.health -= amount

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

    def move(self):
        self.movement = True
        print("The enemy moves!")
        self.movement = False

    def status(self):
        print("%s/5 health left" % self.health)


class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        if self.name in your_inv:
            print("You sell the %s for %s gold" % (self.name, self.money))
            you.money += self.money
            your_inv.remove(self.name)
        else:
            print("You don't have a %s" % self.name)

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Weapon(Item):
    def __init__(self, name, money, damage, speed, health, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.description = description
        self.speed = speed
        self.health = health

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Consumable(Item):
    def __init__(self, heal, mana, name, description, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal
        self.mana = mana
        self.description = description

    def use(self):
        if HealthPotion or RegularManaPotion in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any consumables.")

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Armor(Item):
    def __init__(self, name, health, money):
        super(Armor, self).__init__(name, money)
        self.health = health

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class HeavyArmor(Armor):
    def __init__(self, name, health, money, defense):
        super(HeavyArmor, self).__init__(name, health, money)
        self.defense = defense


class LightArmor(Armor):
    def __init__(self, name, health, money, defense, speed):
        super(LightArmor, self).__init__(name, health, money)
        self.defense = defense
        self.speed = speed


class DangerousArmblades(Weapon):
    def __init__(self, name, damage, ability, attack_type, description, money):
        super(DangerousArmblades, self).__init__(name, description, damage, ability, attack_type, money)
        self.damage = damage
        self.ability = ability
        self.attack_type = attack_type


class HealthHammer(Weapon):
    def __init__(self, name, damage, ability, hp, attack_type, description, money):
        super(HealthHammer, self).__init__(name, description, damage, ability, attack_type, money)
        self.damage = damage
        self.hp = hp
        self.ability = ability
        self.attack_type = attack_type


class SpeedRapier(Weapon):
    def __init__(self, name, damage, ability, speed, attack_type, description, money):
        super(SpeedRapier, self).__init__(name, description, damage, ability, attack_type, money)
        self.damage = damage
        self.ability = ability
        self.speed = speed
        self.attack_type = attack_type


class LesserHealthPotion(Consumable):
    def __init__(self):
            super(LesserHealthPotion, self).__init__("3", "0", "Weaker Healing Potion",
                                                     "A potion the will restore 3 HP.", "50")

    def use(self):
        self.use = True
        self.health = self.health + 3
        self.amount = self.amount - 1
        print("You have used a lesser health potion.")
        self.use = False


class HealthPotion(Consumable):
    def __init__(self):
            super(HealthPotion, self).__init__("5", "0", "Regular Healing Potion", "A potion the will restore 5 HP.",
                                               "100")

    def use(self):
        self.use = True
        self.health = self.health + 5
        self.amount = self.amount - 1
        print("You have used a regular health potion.")
        self.use = False

class GreaterHealthPotion(Consumable):
    def __init__(self):
        super(GreaterHealthPotion, self).__init__("10", "0", "Greater Healing Potion",
                                                  "A potion the will restore 10 HP.", "150")

    def use(self):
        self.use = True
        self.health = self.health + 10
        self.amount = self.amount - 1
        print("You have used a greater health potion.")
        self.use = False


class GreaterManaPotion(Consumable):
    def __init__(self):
        super(GreaterManaPotion, self).__init__("0", "10", "Greater Mana Potion", "A potion the will restore 10 Mana.",
                                                "150")

    def use(self):
        self.use = True
        self.mana = self.mana + 10
        self.amount = self.amount - 1
        print("You have used a greater mana potion.")
        self.use = False


class RegularManaPotion(Consumable):
    def __init__(self):
        super(RegularManaPotion, self).__init__("0", "5", "Regualr Mana Potion", "A potion the will restore 5 Mana.",
                                                "100")

    def use(self):
        self.use = True
        self.mana = self.mana + 5
        self.amount = self.amount - 1
        print("You have used a regular mana potion.")
        self.use = False


class LesserManaPotion(Consumable):
    def __init__(self):
        super(LesserManaPotion, self).__init__("0", "5", "Lesser Mana Potion", "A potion the will restore 3 Mana.", "50")

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


class OffenseBooster(Relic):
    def __init__(self, name, description, ability, damage):
        super(OffenseBooster, self).__init__(name, description, ability)
        self.ability = ability
        self.damage = damage


class HealthBooster(Relic):
    def __init__(self, name, description, hp, ability):
        super(HealthBooster, self).__init__(name, description, ability)
        self.ability = ability
        self.hp = hp


class SpeedBooster(Relic):
    def __init__(self, name, description, ability, speed):
        super(SpeedBooster, self).__init__(name, description, ability)
        self.ability = ability
        self.speed = speed


your_inv = []
max_hp = 100
max_inv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
you = Character("Curious Man", 100, "man in wonder", 10, 0, your_inv)


# Initialize Room
ally_base = Room("ally base", None, "west_ally_safety_zone", "east_ally_safety_zone", "ally_shop", None, None, None,
                 None, "You are at the starting point, Ally_Base", None)
west_ally_safety_zone = Room("west_ally_safety_zone", "west_ally_open_field", None, "ally_base", "ally_base", None,
                             None, "ally_portal", None,
                             "You are at the safety zone for you and your team, West Ally Safety Zone.", None)
east_ally_safety_zone = Room("east_ally_safety_zone", "east_ally_open_field", "ally_base", None, None, "ally_base",
                             None, None, "ally portal",
                             "You are at the safety zone for you and your team, East Ally Safety Zone.", None)
ally_shop = Room("ally_shop", "ally_base", None, None, None, None, None, None, None,
                 "You are at the shop for allies where you buy items.", None)
west_ally_open_field = Room("west_ally_open_field", "jungle_camp_speed_west", None, "middle_combat_field",
                            "west_ally_safety_zone", None, None, None, None,
                            "You are at the west open field where you can fight but it is the outskirts of this place."
                            , None)
east_ally_open_field = Room("east_ally_open_field", "jungle_camp_speed east", None, None, "east safety zone", None,
                            None, None, "middle combat field",
                            "You are at the east open field where you can fight but it is the outskirts of this place.",
                            None)
jungle_camp_mana_west = Room("jungle camp mana west", "jungle camp attack west", "behind the west camps",
                             "middle combat field", "west ally open field", None, None, None, None,
                             "You are at the jungle camp where you can kill a monster for a timed mana regen boost.",
                             "West Mana Sentinal")
jungle_camp_speed_east = Room("jungle camp speed east", "middle combat field", "behind the east camps",
                              "east ally open field", None, None, None, None, None,
                              "You are at the jungle camp where you can kill a monster for a timed speed boost.",
                              "Speed Raptor")
jungle_camp_attack_west = Room("jungle camp attack west", "jungle camp speed west", "behind the west camps",
                               "middle combat field", "jungle camp mana west", None, None, None, None,
                               "You are at the jungle camp where you can kill a monster for a timed attack boost.",
                               "Attack Ogre")
jungle_camp_attack_east = Room("jungle camp attack east", "jungle camp speed east", "middle combat field",
                               "behind the east camps", "jungle camp mana east", None, None, None, None,
                               "You are at the jungle camp where you can kill a monser for a timed attack boost.",
                               "Attack Ogre")
jungle_camp_mana_east = Room("jungle camp mana east", "jungle camp attack east", "middle combat field",
                             "behind the east camps", "east ally open field", None, None, None, None,
                             "You are at the jungle camp where you can kil a monster for a timed mana boost",
                             "Mana Sentinal")
jungle_camp_speed_west = Room("jungle camp speed west", "east enemy open field", "middle combat field,",
                              "behind the east camps", "jungle camp attack west", None, None, None, None,
                              "You are at the west jungle camp where you can kil a monster for a timed speed boost",
                              "Speed Raptor")
behind_the_camps_west = Room("behind the camps west", "jungle camp mana west", None, "jungle camp attack west",
                             "jungle camp speed west", None, None, None, None,
                             "You are behind the jungle camps of the west.", None)
behind_the_camps_east = Room("behind the camps east", "jungle camp speed east", "jungle camp attack east",
                             None, "jungle camp mana east", None, None, None, None,
                             "You are behind the jungle camps of the east.", None)
enemy_base = Room(" enemy base", "enemy shop", "east enemy safety zone", "west enemy safety zone", None, None, None,
                  None, None, "You are at the ending point, Enemy Base", "Enemy Champion")
west_enemy_safety_zone = Room("west enemy safety zone", "enemy base", None, "enemy base", "west enemy open field",
                              "enemy portal", None, None, None,
                              "You are at the safety zone for you and your team, West Enemy Safety Zone.", None)
east_enemy_safety_zone = Room("east enemy safety zone", "enemy base", "enemy portal", "enemy base",
                              "east enemy open field", None, None, None, None,
                              "You are at the safety zone for you and your team, East Enemy Safety Zone.", None)
enemy_shop = Room("enemy shop", None, None, None, "enemy base", None, None, None, None,
                  "You are at the shop for allies where you buy items.", None)
west_enemy_open_field = Room("west enemy open field", "west enemy safety zone", "middle combat field", None,
                             "jungle camp speed west", None, None, None, None,
                             "You are at the west open field where you can fight but it is the outskirts of this "
                             "place.", None)
east_enemy_open_field = Room("east enemy open field", "right enemy safety zone", None, "middle combat field",
                             "jungle camp speed east", None, None, None, None,
                             "You are at the east open field where you can fight but it is the outskirts of this"
                             " place.", None)
ally_portal = Room("ally portal", "middle combat field", "left ally safety zone", "right ally safety zone", None, None,
                   None, None, None, "You are at your portal. Protect your portal by stopping minions from entering.",
                   None)
enemy_portal = Room("enemy portal", None, "Right enemy safety zone", "left enemy safety zone", "middle combat field",
                    None, None, None, None, "You are at the enemy portal. Clear a path for your minions to enter the "
                                            "portal.", "Enemy Minions")
middle_of_combat_field = Room("middle combat field", None, "jungle camp attack west", "jungle camp attack east", None,
                              "ally open field east", "ally open field west", "enemy open field east",
                              "enemy open field west", "You are at the combat field. The middle of the map. This is "
                              "where you fight.", "Enemy Minions" "Aly Minions")


current_node = ally_base
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']
all_the_commands = ['buy', 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast',
                    'se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne', 'hp', 'money', 'help', 'inv', 'fight', 'stats', 'me',
                    'sell', 'buy', 'heal', 'fight evil']

character_name = input('What is your name?\n>_')
you.name = character_name
character_description = input('Describe yourself?\na:')
you.description = ('a' + ' ' + character_description)

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long term
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
    else:
        print("Command not recognized.")