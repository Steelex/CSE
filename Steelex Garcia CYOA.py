import random
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
    def __init__(self, name, health, mana, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.mana = mana
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
    def __init__(self, name, description, ability, attack_speed):
        super(SpeedBooster, self).__init__(name, description, ability)
        self.ability = ability
        self.attack_speed = attack_speed


your_inv = []
max_hp = 100
max_mana = 100
max_inv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
you = Character("Curious Man", 100, 100, "man in wonder", 10, 0, your_inv)


def fight(self, enemy):
    try:
        if enemy == current_node.enemy_in:
            print(you.name + ",", you.description, "starts fighting with %s" % enemy.name + ",", enemy.description)
            enemy.health = enemy.orig_hp
            while enemy.health != 0:
                choice = random.choice([enemy, self])
                if choice == self:
                    enemy.hit(self)
                    if you.health > max_hp:
                        you.health = max_hp
                elif choice == enemy:
                    self.hit(enemy)
            print()
    except AttributeError:
        print("There are no enemies.")


# Initialize Room
ally_base = Room("ally base", None, "west_ally_safety_zone", "east_ally_safety_zone", "ally_shop", None, None, None,
                 None, "You are at the starting point, Ally_Base", None)
west_ally_safety_zone = Room("west_ally_safety_zone", "west_ally_open_field", None, "ally_base", "ally_base", None,
                             None, "ally_portal", None,
                             "You are at the safety zone for you and your team, West Ally Safety Zone.", None)
east_ally_safety_zone = Room("east_ally_safety_zone", "east_ally_open_field", "ally_base", None, None, "ally_base",
                             None, None, "ally_portal",
                             "You are at the safety zone for you and your team, East_Ally_Safety_Zone.", None)
ally_shop = Room("ally_shop", "ally_base", None, None, None, None, None, None, None,
                 "You are at the shop for allies where you buy items.", None)
west_ally_open_field = Room("west_ally_open_field", "jungle_camp_speed_west", None, "middle_combat_field",
                            "west_ally_safety_zone", None, None, None, None,
                            "You are at the west open field where you can fight but it is the outskirts of this place."
                            , None)
east_ally_open_field = Room("east_ally_open_field", "jungle_camp_speed_east", None, None, "east_safety_zone", None,
                            None, None, "middle_combat_field",
                            "You are at the east open field where you can fight but it is the outskirts of this place.",
                            None)
jungle_camp_mana_west = Room("jungle_camp_mana_west", "jungle_camp_attack_west", "behind_the_west_camps",
                             "middle_combat_field", "west_ally_open field", None, None, None, None,
                             "You are at the jungle camp where you can kill a monster for a timed mana regen boost.",
                             "West Mana Sentinal")
jungle_camp_speed_east = Room("jungle_camp_speed_east", "middle_combat_field", "behind_the_east_camps",
                              "east_ally_open_field", None, None, None, None, None,
                              "You are at the jungle camp where you can kill a monster for a timed speed boost.",
                              "Speed Raptor")
jungle_camp_attack_west = Room("jungle_camp_attack_west", "jungle_camp_speed_west", "behind_the_west_camps",
                               "middle_combat_field", "jungle_camp_mana_west", None, None, None, None,
                               "You are at the jungle camp where you can kill a monster for a timed attack boost.",
                               "Attack Ogre")
jungle_camp_attack_east = Room("jungle_camp_attack_east", "jungle_camp_speed_east", "middle_combat_field",
                               "behind_the_east_camps", "jungle_camp_mana_east", None, None, None, None,
                               "You are at the jungle camp where you can kill a monser for a timed attack boost.",
                               "Attack Ogre")
jungle_camp_mana_east = Room("jungle_camp_mana_east", "jungle_camp_attack_east", "middle_combat_field",
                             "behind_the_east_camps", "east_ally_open_field", None, None, None, None,
                             "You are at the jungle camp where you can kil a monster for a timed mana boost",
                             "Mana Sentinal")
jungle_camp_speed_west = Room("jungle_camp_speed_west", "east_enemy_open_field", "middle_combat_field,",
                              "behind_the_east_camps", "jungle_camp_attack_west", None, None, None, None,
                              "You are at the west jungle camp where you can kil a monster for a timed speed boost",
                              "Speed Raptor")
behind_the_camps_west = Room("behind_the_camps_west", "jungle_camp_mana_west", None, "jungle_camp_attack_west",
                             "jungle_camp_speed_west", None, None, None, None,
                             "You are behind the jungle camps of the west.", None)
behind_the_camps_east = Room("behind_the_camps_east", "jungle_camp_speed_east", "jungle_camp_attack_east",
                             None, "jungle_camp_mana_east", None, None, None, None,
                             "You are behind the jungle camps of the east.", None)
enemy_base = Room("enemy_base", "enemy_shop", "east_enemy_safety_zone", "west_enemy_safety_zone", None, None, None,
                  None, None, "You are at the ending point, Enemy_Base", "Enemy_Champion")
west_enemy_safety_zone = Room("west_enemy_safety_zone", "enemy_base", None, "enemy_base", "west_enemy_open_field",
                              "enemy_portal", None, None, None,
                              "You are at the safety zone for you and your team, West Enemy Safety Zone.", None)
east_enemy_safety_zone = Room("east_enemy_safety_zone", "enemy_base", "enemy_portal", "enemy_base",
                              "east_enemy_open_field", None, None, None, None,
                              "You are at the safety zone for you and your team, East Enemy Safety Zone.", None)
enemy_shop = Room("enemy_shop", None, None, None, "enemy_base", None, None, None, None,
                  "You are at the shop for allies where you buy items.", None)
west_enemy_open_field = Room("west_enemy_open_field", "west_enemy_safety_zone", "middle_combat_field", None,
                             "jungle_camp_speed_west", None, None, None, None,
                             "You are at the west open field where you can fight but it is the outskirts of this "
                             "place.", None)
east_enemy_open_field = Room("east_enemy_open_field", "right_enemy_safety_zone", None, "middle_combat_field",
                             "jungle_camp_speed_east", None, None, None, None,
                             "You are at the east open field where you can fight but it is the outskirts of this"
                             " place.", None)
ally_portal = Room("ally_portal", "middle_combat_field", "left_ally_safety_zone", "right_ally_safety_zone", None, None,
                   None, None, None, "You are at your portal. Protect your portal by stopping minions from entering.",
                   None)
enemy_portal = Room("enemy_portal", None, "Right_enemy_safety_zone", "left_enemy_safety_zone", "middle_combat_field",
                    None, None, None, None, "You are at the enemy portal. Clear a path for your minions to enter the "
                                            "portal.", "Enemy Minions")
middle_of_combat_field = Room("middle_combat_field", None, "jungle_camp_attack_west", "jungle_camp_attack_east", None,
                              "ally_open_field_east", "ally_open_field_west", "enemy_open_field_east",
                              "enemy_open_field_west", "You are at the combat field. The middle of the map. This is "
                              "where you fight.", "Enemy Minions" "Aly Minions")


current_node = ally_base
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']
all_the_commands = ['buy', 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast',
                    'se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne', 'hp', 'money', 'help', 'inv', 'fight', 'stats',
                    'sell', 'buy', 'heal', 'attack']

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


    if command == 'quit':
        exit(0)

    if command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]

    if command == 'money':
        print(you.money)

    if command == 'help':
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw', "
              "'s', 'w', 'e', 'n', 'sw', 'ne' to move.")

    if command == 'inv':
        for i in your_inv:
            print('[ ' + i.name + ' ]')
        if len(your_inv) == 0:
            print([])

    if command == 'fight':
        you.fight(current_node.enemy_in)

    if command == 'heal':
        if HealthPotion in your_inv:
            if you.health == max_hp:
                print("You are already full hp.")
            if you.health < max_hp:
                print("You drink a health potion.")
                you.health += HealthPotion.heal
                if you.health > max_hp:
                    you.health = max_hp
            print('HP: %s' % you.health)
        else:
            "You don\'t have a health potion."
        if HealthPotion not in your_inv:
            print("You don\'t have a health potion.")
