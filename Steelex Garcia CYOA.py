import random


class Room(object):
    def __init__(self, name, north, west, east, south, se, sw, ne, nw, description, enemy):
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
        self.enemy = enemy

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
    def __init__(self, name, money, attack):
        self.name = name
        self.money = money
        self.attack = attack

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

    def hit(self, target):
        target.take_damage(self)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if you.health <= 0:
            print('You died.')
            exit(0)
        if target.health <= 0:
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            print('HP: %s' % you.health)
            self.money += target.money
            if target.health < 0:
                target.health = 0
            # Loot
            choice = random.randint(1, 20)
            loot = random.randint(1, 20)
            if choice == loot:
                your_inv.append(target.inventory)


class Weapon(Item):
    def __init__(self, name, money, attack, description):
        super(Weapon, self).__init__(name, money, attack)
        self.attack = attack
        self.description = description


    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Consumable(Item):
    def __init__(self, name, description, money):
        super(Consumable, self).__init__(name, money, None)
        self.description = description

    def heal(self):
        if HealthPotion or LesserHealthPotion or GreaterHealthPotion in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any health potions.")

    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You're broke. Get some more money")


class Armor(Item):
    def __init__(self, name, health, money, description):
        super(Armor, self).__init__(name, health, money)
        self.health = health
        self.description = description

    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class HeavyArmor(Armor):
    def __init__(self, name, health, money, description):
        super(HeavyArmor, self).__init__(name, health, money, description)
        self.description = description


class LightArmor(Armor):
    def __init__(self, name, health, money, description, speed):
        super(LightArmor, self).__init__(name, health, money, description)
        self.speed = speed
        self.description = description


class DangerousArmblades(Weapon):
    def __init__(self,name, money, attack, description):
        super(DangerousArmblades, self).__init__(name, money, attack, description)
        self.attack = attack
        self.description = description


class HealthHammer(Weapon):
    def __init__(self, name, money, attack, description, health):
        super(HealthHammer, self).__init__(name, money, attack, description)
        self.health = health
        self.attack = attack


class SpeedRapier(Weapon):
    def __init__(self, name, money, attack, description, speed):
        super(SpeedRapier, self).__init__(name, money, attack, description)
        self.speed = speed
        self.attack = attack


class HealthPotion(Consumable):
    def __init__(self, name, description, money, heal):
        super(HealthPotion, self).__init__(name, description, money)
        self.heal = heal


class GreaterHealthPotion(Consumable):
    def __init__(self, name, description, money, heal):
        super(GreaterHealthPotion, self).__init__(name, description, money)
        self.heal = heal

class LesserHealthPotion(Consumable):
    def __init__(self, name, description, money, heal):
        super(LesserHealthPotion, self).__init__(name, description, money)
        self.heal = heal


class Relic(Item):
    def __init__(self, name, description, money):
        super(Relic, self).__init__(name, description, None)
        self.money = money

class OffenseBooster(Relic):
    def __init__(self, name, description, money, attack):
        super(OffenseBooster, self).__init__(name, description, money)
        self.attack = attack
        self.money = money


class HealthBooster(Relic):
    def __init__(self, name, description, money, health):
        super(HealthBooster, self).__init__(name, description, money)
        self.health = health
        self.money = money


class SpeedBooster(Relic):
    def __init__(self, name, description, money, speed):
        super(SpeedBooster, self).__init__(name, description, money)
        self.speed = speed
        self.money = money


HeavyArmor = HeavyArmor("HeavyArmor", 800, 2350, "Armor for people that tank damage. It's big, heavy, and sturdy.")
LightArmor = LightArmor("LightArmor", 500, 2200, "Armor for people that move alot. Its light and strong.", 50)
DangerousArmblades = DangerousArmblades("DangerousArmblades", 2000, 250,
                                        "A very dangerous armblade that cuts through everything")
HealthHammer = HealthHammer("HealthHammer", 2000, 125, "A huge hammer strong and sturdy hammer that gives health.", 400)
SpeedRapier = SpeedRapier("SpeedRapier", 2000, 125, "A quick, strong, and powerful weapon that makes moving easier.",
                          100)
SpeedBooster = SpeedBooster("SpeedBooster", "A relic that boosts your speed", 950, 50)
OffenseBooster = OffenseBooster("OffenseBooser", "A relic that boosts your attack",950, 50)
HealthBooster = HealthBooster("HealthBooster", "A relic that boosts your health", 950, 200)
HealthPotion = HealthPotion("HealthPotion", )

your_inv = []
max_health = 100
max_mana = 100
max_inventory = [1, 2, 3, 4, 5, 6, 7]
you = Character("Curious Man", 100, 100, "man in wonder", 10, 0, your_inv)


def fight(self, enemy):
    try:
        if enemy == current_node.enemy:
            print(you.name + ",", you.description, "starts fighting with %s" % enemy.name + ",", enemy.description)
            enemy.health = enemy.orig_hp
            while enemy.health != 0:
                choice = random.choice([enemy, self])
                if choice == self:
                    enemy.hit(self)
                    if you.health > max_health:
                        you.health = max_health
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
                            "You are at the west open field where you can fight but it is the outskirts of this place.",
                            None)
east_ally_open_field = Room("east_ally_open_field", "jungle_camp_speed_east", "middle_combat_field", None,
                            "east_safety_zone", None, None, None, "middle_combat_field",
                            "You are at the east open field where you can fight but it is the outskirts of this place.",
                            None)
jungle_camp_mana_west = Room("jungle_camp_mana_west", "jungle_camp_attack_west", "behind_the_west_camps",
                             "middle_combat_field", "west_ally_open field", None, None, None, None,
                             "You are at the jungle camp where you can kill a monster for a timed mana regen boost.",
                             "West Mana Sentinal")
jungle_camp_speed_east = Room("jungle_camp_speed_east", "east_enemy_open_field", "behind_the_east_camps",
                              None, "jungle_camp_attack_east", None, None, None, None,
                              "You are at the jungle camp where you can kill a monster for a timed speed boost.",
                              "Speed Raptor")
jungle_camp_attack_west = Room("jungle_camp_attack_west", "jungle_camp_mana_west", "behind_the_west_camps",
                               "middle_combat_field", "jungle_camp_speed_west", None, None, None, None,
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
jungle_camp_speed_west = Room("jungle_camp_speed_west", "west_enemy_open_field", "middle_combat_field,",
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
enemy_portal = Room("enemy_portal", "ally_base", "ally_base", "ally_base", "ally_base", "ally_base", "ally_base",
                    "ally_base", "ally_base", "You entered the enemy portal. You will be teleported back to base for "
                                              "safety", "Enemy Minions")
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
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw',"
              " 's', 'w', 'e', 'n', 'sw', 'ne' to move.")


    if command == 'buy':
        armor_shop = [HeavyArmor, LightArmor]
        weapon_shop = [DangerousArmblades, SpeedRapier, HealthHammer]
        shop = [HeavyArmor, LightArmor, DangerousArmblades, SpeedRapier, HealthHammer, SpeedBooster, OffenseBooster,
                HealthBooster, LesserHealthPotion, HealthPotion, GreaterHealthPotion]

        if current_node == ally_shop:

            print("---SHOP---"
                  "\n_________________________________________________________________________________"
                  "\nHeavyArmor(0) DangerousArmblades(1) OffenseBooster(2) HealthBooster(3)\n"
                  " 2350 Money      "
                  "\n_______________________________________"
                  "__________________________________________\n")

            item_buying = input("What do you want to buy? (Type in the number)\nYOUR MONEY: %s\n>_" % you.money)
            try:
                item_buy = shop[int(item_buying)]
                if you.money < item_buy.money:
                    print("You're poor. Go farm some more fo moneys.")
                if you.money >= item_buy.money:
                    print("You buy a %s. %s" % (item_buy.name, item_buy.description))
                    your_inv.append(item_buy)
                    you.money -= item_buy.money
                    if item_buy in armor_shop:
                        max_health += item_buy.health
                print("That is not an item.")
            except IndexError:
                print("That is not an item.")

        elif current_node != ally_shop:
            print('You are not in the shop.')

    if command == 'inv':
        for i in your_inv:
            print('[ ' + i.name + ' ]')
        if len(your_inv) == 0:
            print([])

    if command == 'fight':
        you.attack(current_node.enemy)

    if command == 'heal':
        if HealthPotion not in your_inv:
            print("You don\'t have a health potion.")
        if HealthPotion in your_inv:
            if you.health == max_health:
                print("You are already full hp.")
            if you.health < max_health:
                print("You drink a health potion.")
                you.health += HealthPotion.heal
                if you.health > max_health:
                    you.health = max_health
            print('HP: %s' % you.health)
        else:
            "You don\'t have a health potion."
