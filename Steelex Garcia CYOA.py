
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

    def interact(self):
        print(self.name)
        print(self.description)
        print(self.health)

    def move(self):
        self.movement = True
        print("The enemy moves!")
        self.movement = False

    def status(self):
        print("%s/5 health left" % self.health)

    def attack(self, target):
        target.take_damage(self.attack)
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

    def fight(self, enemy):
        if enemy.health > 0:
            print("You attack for %d damage" % you.attack)
            current_node.enemy.health = current_node.enemy.health - you.attack
        if current_node.enemy.health <= 0:
            current_node.enemy.health = 0
            print("The enemy is already dead, there is nothing else for you to fight.")
            print('%s died.' % enemy.name)
            print('You received %s gold.' % enemy.money)
            print('HP: %s' % you.health)
            self.money += enemy.money
            if enemy.health < 0:
                enemy.health = 0
        if current_node.enemy is None:
            print("There are no enemies in this room.")

    def take_damage(self, you):
        if you.health > 0:
            print("The enemy attacks you.")
            you.health = you.health - current_node.enemy.attack
            print("You lost %d health!" % current_node.enemy.attack)
        if you.attack > 0:
            print("Current Health: %d" % you.health)


class Enemy(Character):
    def __init__(self, name, health, mana, description, attack, money, inventory):
        super(Enemy, self).__init__(name, health, mana, description, attack, money, inventory)
        self.attack = attack
        self.health = health
        self.description = description
        self.money = money
        self.name = name


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

    def attack(self, target):
        target.take_damage(self)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if you.health <= 0:
            print('You died.')
            quit(0)
        if target.health <= 0:
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            print('HP: %s' % you.health)
            self.money += target.money
            if target.health < 0:
                target.health = 0


class Weapon(Item):
    def __init__(self, name, money, attack, description):
        super(Weapon, self).__init__(name, money, attack)
        self.attack = attack
        self.description = description

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
    def __init__(self, name, money, attack, description, health):
        super(DangerousArmblades, self).__init__(name, money, attack, description)
        self.attack = attack
        self.description = description
        self.health = health

class MetalSword(Weapon):
    def __init___(self, name, money, attack, description, health):
        super(MetalSword, self).__init__(name, money, attack, description)
        self.attack = attack
        self.health = health

class HealthHammer(Weapon):
    def __init__(self, name, money, attack, description, health):
        super(HealthHammer, self).__init__(name, money, attack, description)
        self.health = health
        self.attack = attack


class SpeedRapier(Weapon):
    def __init__(self, name, money, attack, description, speed, health):
        super(SpeedRapier, self).__init__(name, money, attack, description)
        self.speed = speed
        self.attack = attack
        self.health = health


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
        super(Relic, self).__init__(name, description, 0)
        self.money = money
        self.description = description


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


HeavyArmor = HeavyArmor("HeavyArmor", 2350, 800, "Armor for people that tank damage. It's big, heavy, and sturdy.")
LightArmor = LightArmor("LightArmor", 2200, 500, "Armor for people that move alot. Its light and strong.", 50)
DangerousArmblades = DangerousArmblades("DangerousArmblades", 2000, 350,
                                        "A very dangerous armblade that cuts through everything", 0)
HealthHammer = HealthHammer("HealthHammer", 2000, 200, "A huge hammer strong and sturdy hammer that gives health.", 400)
SpeedRapier = SpeedRapier("SpeedRapier", 2000, 200, "A quick, strong, and powerful weapon that makes moving easier.",
                          100, 0)
SpeedBooster = SpeedBooster("SpeedBooster", "A relic that boosts your speed", 950, 50)
OffenseBooster = OffenseBooster("OffenseBooster", "A relic that boosts your attack", 950, 50)
HealthBooster = HealthBooster("HealthBooster", "A relic that boosts your health", 950, 200)
HealthPotion = HealthPotion("HealthPotion", "A medium sized health potion", 100, 200)
LesserHealthPotion = LesserHealthPotion("LesserHealthPotion", "A smaller sized health potion", 50, 100)
GreaterHealthPotion = GreaterHealthPotion("GreaterHealthPotion", "A big sized health potion", 300, 500)
MetalSword = MetalSword("MetalSword", 100, 150, "A regular metal sword used for fighting")

your_inv = []
health = 100
max_mana = 100
max_inventory = []
you = Character("?", 100, 100, "?", 50, 10000, your_inv)
offense = ['fight']

Attack_Ogre = Enemy("Attack_Ogre", 1000, None, "An ogre that you kill and gets you an attack buff raising your attack.",
                    20, 250, None)
Enemy_Minion = Enemy("Enemy_Minion", 100, None, "A minion you can use to farm.", 5, 50, None)
Speed_Raptor = Enemy("Speed_Raptor", 800, None, "A raptor that you kill and gets you a speed buff raising your speed",
                     10, 250, None)
Mana_Sentinal = Enemy("Mana_Sentinal", 900, None, "A sentinal that you kill and gets you mana regen", 15, 250, None)
Enemy_Boss_Champion = Enemy("Enemy_Boss_Champion", 5000, None, "The enemy Boss champion. The strongest enemy there is.",
                            90, 10000, None)
Enemy_Champion = Enemy("Enemy_Champion", 2500, None, "An enemy champion. It's hard to kill.", 40, 5000, None)
ENEMY_shop_BAWS = Enemy("ENEMY_shop_BAWS", 1, None, "He's health is low but his attack is high, Plus he's filthy rich.",
                        1000, 99999999, None)

# Initialize Room
ally_base = Room("ally base", None, "west_ally_safety_zone", "east_ally_safety_zone", "ally_shop", None, None, None,
                 None, "You are at the starting point, Ally_Base. There are no enemies.", None)
west_ally_safety_zone = Room("west_ally_safety_zone", "west_ally_open_field", None, "ally_base", "ally_base", None,
                             None, "ally_portal", None,
                             "You are at the safety zone for you and your team, West Ally Safety Zone."
                             " There are no enemies", None)
east_ally_safety_zone = Room("east_ally_safety_zone", "east_ally_open_field", "ally_base", None, None, "ally_base",
                             None, None, "ally_portal",
                             "You are at the safety zone for you and your team, East_Ally_Safety_Zone."
                             " There are no enemies", None)
ally_shop = Room("ally_shop", "ally_base", None, None, None, None, None, None, None,
                 "You are at the shop for allies where you buy items. There are no enemies", None)
west_ally_open_field = Room("west_ally_open_field", "jungle_camp_mana_west", None, "middle_of_combat_field",
                            "west_ally_safety_zone", None, None, None, None,
                            "You are at the west open field where you can fight but it is the outskirts of this place."
                            " There are no enemies", None)
east_ally_open_field = Room("east_ally_open_field", "jungle_camp_speed_east", "middle_of_combat_field", None,
                            "east_ally_safety_zone", None, None, None, "middle_of_combat_field",
                            "You are at the east open field where you can fight but it is the outskirts of this place."
                            " There are no enemies", None)
jungle_camp_mana_west = Room("jungle_camp_mana_west", "jungle_camp_attack_west", "behind_the_west_camps",
                             "middle_of_combat_field", "west_ally_open field", None, None, None, None,
                             "You are at the jungle camp where you can kill a monster for a timed mana regen boost.",
                             Mana_Sentinal)
jungle_camp_speed_east = Room("jungle_camp_speed_east", "jungle_camp_attack_east", "behind_the_east_camps",
                              None, "jungle_camp_attack_east", None, None, None, None,
                              "You are at the jungle camp where you can kill a monster for a timed speed boost."
                              " You see a Speed Raptor", Speed_Raptor)
jungle_camp_attack_west = Room("jungle_camp_attack_west", "jungle_camp_speed_west", "behind_the_west_camps",
                               "middle_of_combat_field", "jungle_camp_mana_west", None, None, None, None,
                               "You are at the jungle camp where you can kill a monster for a timed attack boost."
                               " You see an Attack Ogre", Attack_Ogre)
jungle_camp_attack_east = Room("jungle_camp_attack_east", "jungle_camp_mana_east", "middle_of_combat_field",
                               "behind_the_east_camps", "jungle_camp_mana_east", None, None, None, None,
                               "You are at the jungle camp where you can kill a monser for a timed attack boost."
                               " You see an attack Ogre", Attack_Ogre)
jungle_camp_mana_east = Room("jungle_camp_mana_east", "east_enemy_open_field", "middle_of_combat_field",
                             "behind_the_east_camps", "east_ally_open_field", None, None, None, None,
                             "You are at the jungle camp where you can kil a monster for a timed mana boost."
                             " You see a Mana Sentinal", Mana_Sentinal)
jungle_camp_speed_west = Room("jungle_camp_speed_west", "west_enemy_open_field", "middle_of_combat_field,",
                              "behind_the_east_camps", "jungle_camp_attack_west", None, None, None, None,
                              "You are at the west jungle camp where you can kil a monster for a timed speed boost. "
                              "You see a Speed Raptor", Speed_Raptor)
behind_the_camps_west = Room("behind_the_camps_west", "jungle_camp_mana_west", None, "jungle_camp_attack_west",
                             "jungle_camp_speed_west", None, None, None, None,
                             "You are behind the jungle camps of the west. There are no enemies", None)
behind_the_camps_east = Room("behind_the_camps_east", "jungle_camp_speed_east", "jungle_camp_attack_east",
                             None, "jungle_camp_mana_east", None, None, None, None,
                             "You are behind the jungle camps of the east. There are no enemies", None)
enemy_base = Room("enemy_base", "enemy_shop", "east_enemy_safety_zone", "west_enemy_safety_zone", None, None, None,
                  None, None, "You are at the ending point, Enemy Base. You see THE BOSS CHAMPION", Enemy_Boss_Champion)
west_enemy_safety_zone = Room("west_enemy_safety_zone", "enemy_base", None, "enemy_base", "west_enemy_open_field",
                              "enemy_portal", None, None, None,
                              "You are at the safety zone for you and your team, West Enemy Safety Zone."
                              " You see an enemy champion", Enemy_Champion)
east_enemy_safety_zone = Room("east_enemy_safety_zone", "enemy_base", "enemy_portal", "enemy_base",
                              "east_enemy_open_field", None, None, None, None,
                              "You are at the safety zone for you and your team, East Enemy Safety Zone."
                              " You see an enemy champion.", Enemy_Champion)
enemy_shop = Room("enemy_shop", None, None, None, "enemy_base", None, None, None, None,
                  "You are at the shop for allies where you buy items.", ENEMY_shop_BAWS)
west_enemy_open_field = Room("west_enemy_open_field", "west_enemy_safety_zone", "middle_of_combat_field", None,
                             "jungle_camp_speed_west", None, None, None, None,
                             "You are at the west open field where you can fight but it is the outskirts of this "
                             "place.", Enemy_Minion)
east_enemy_open_field = Room("east_enemy_open_field", "east_enemy_safety_zone", None, "middle_of_combat_field",
                             "jungle_camp_speed_east", None, None, None, None,
                             "You are at the east open field where you can fight but it is the outskirts of this"
                             " place. You see an Enemy Minion", Enemy_Minion)
ally_portal = Room("ally_portal", "middle_of_combat_field", "left_ally_safety_zone", "right_ally_safety_zone", None,
                   None, None, None, None, "You are at your portal.", None)
enemy_portal = Room("enemy_portal", "ally_base", "ally_base", "ally_base", "ally_base", "ally_base", "ally_base",
                    "ally_base", "ally_base", "You entered the enemy portal. You will be teleported back to base for "
                    "safety. You see an enemy minion", Enemy_Minion)
middle_of_combat_field = Room("middle_of_combat_field", "ally_portal", "jungle_camp_attack_west",
                              "jungle_camp_attack_east", "enemy_portal", "ally_open_field_east", "ally_open_field_west",
                              "enemy_open_field_east", "enemy_open_field_west",
                              "You are at the combat field. The middle of the map.", Enemy_Minion)


current_node = ally_base
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']
all_the_commands = ['buy', 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast',
                    'se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne', 'hp', 'money', 'help', 'inv', 'fight', 'stats',
                    'sell', 'buy', 'heal']

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

    if command == 'stats':
        print('-------------------------------------------------------------------------------------------------------')
        print('Current Health' + ' - ' + str(health))
        print('Attack' + ' - ' + str(you.attack))
        print('-------------------------------------------------------------------------------------------------------')

    if command == 'me':
        print('-----------------------------------------------------------------------------------------------------\n')
        print(you.name)
        print(you.description)
        print('\n-----------------------------------------------------------------------------------------------------')

    if command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]

    if command == 'money':
        print('\n-----------------------------------------------------------------------------------------------------')
        print(" %s Moneys" % you.money)
        print('\n-----------------------------------------------------------------------------------------------------')

    if command == 'help':
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw',"
              " 's', 'w', 'e', 'n', 'sw', 'ne' to move.")

    if command == 'buy':
        armor_shop = [HeavyArmor, LightArmor]
        weapon_shop = [DangerousArmblades, SpeedRapier, HealthHammer]
        shop = [HeavyArmor, DangerousArmblades, OffenseBooster, HealthBooster, SpeedBooster, LightArmor, SpeedRapier,
                HealthHammer, MetalSword, LesserHealthPotion, GreaterHealthPotion, HealthPotion]

        if current_node == ally_shop:

            print("---SHOP---"
                  "\n______________________________________________________________________________ \n"
                  "\n HeavyArmor(0)2350 Moneys   DangerousArmblades(1)2000 Moneys   OffenseBooster(2)950 Moneys\n"
                  "\n HealthBooster(3)950 Moneys   SpeedBooster(4)950 Moneys   LightArmor(5)2200 Moneys\n"
                  "\n SpeedRapier(6)2000 Moneys   HealthHammer(7)2000 Moneys   MetalSword(8)150 Moneys\n"
                  "\n LesserHealthPotion(9)50 Moneys   GreaterHealthPotion(10)300 Moneys   HealthPotion(11)150 Moneys\n"
                  "\n_______________________________________"
                  "__________________________________________\n")

            item_buying = input("What do you want to buy? (Type in the number)\nYour Moneys: %s\n>_" % you.money)
            try:
                item_buy = shop[int(item_buying)]
                if you.money < item_buy.money:
                    print("You're poor. Go farm some more fo moneys.")
                if you.money >= item_buy.money:
                    print("You bought a %s. %s" % (item_buy.name, item_buy.description))
                    your_inv.append(item_buy)
                    you.money -= item_buy.money
                    if item_buy in armor_shop:
                        you.health += item_buy.health
                    if item_buy in weapon_shop:
                        you.attack += item_buy.attack
                        if item_buy.health > 0:
                            you.health += item_buy.health
            except ValueError:
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
        if current_node.enemy is not None and current_node.enemy.health > 0:
            you.fight(current_node.enemy)
            you.take_damage(you)

    if you.health <= 0:
        print("You have died... "
              "Good Game. Game Over. Sad life. You Failed.")
        quit(0)

    if command == 'quit':
        quit(0)

    if command == 'heal':
        if HealthPotion not in your_inv:
            print("You don\'t have a health potion.")
        if HealthPotion in your_inv:
            if you.health == health:
                print("You are already full hp.")
            if you.health < health:
                print("You drink a health potion.")
                you.health += HealthPotion.heal
                if you.health > health:
                    you.health = health
            print('HP: %s' % you.health)
        else:
            "You don\'t have a health potion."
        if GreaterHealthPotion not in your_inv:
            print("You don\'t have a greater health potion.")
        if GreaterHealthPotion in your_inv:
            if you.health == health:
                print("You are already full hp.")
            if you.health < health:
                print("You drink a greater health potion.")
                you.health += HealthPotion.heal
                if you.health > health:
                    you.health = health
            print('HP: %s' % you.health)
        else:
            "You don\'t have a greater health potion."
        if LesserHealthPotion not in your_inv:
            print("You don\'t have a lesser health potion.")
        if LesserHealthPotion in your_inv:
            if you.health == health:
                print("You are already full hp.")
            if you.health < health:
                print("You drink a lesser health potion.")
                you.health += HealthPotion.heal
                if you.health > health:
                    you.health = health
            print('HP: %s' % you.health)
        else:
            "You don\'t have a lesser health potion."
