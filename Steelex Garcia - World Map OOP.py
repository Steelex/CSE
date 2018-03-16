class Room(object):
    def __init__(self, name, north, west, east, south, se, sw, ne, nw, description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

class Item(object):
    def __init__(self, name, description):


class Armor(Item):


class Heavy_Armor(object):
    def __init__(self, name, description):
        super(Heavy_Armor, self).__init__(name, description)

class Light_Armor(object):
    def __init__(self, name, description):
        super(Light_Armor, name, description)



# Initialize Room
ally_base = Room("ally base", None, "west ally safety zone", "east ally safety zone", "ally shop", None, None, None,
                 None, "You are at the starting point, Ally Base")
west_ally_safety_zone = Room("west ally safety zone", "west ally open field", None, "ally base", "ally base", None,
                             None, "ally portal", None,
                             "You are at the safety zone for you and your team, West Ally Safety Zone.")
east_ally_safety_zone = Room("east ally safety zone", "east ally open field", "ally base", None, None, "ally base",
                             None, None, "ally portal",
                             "You are at the safety zone for you and your team, East Ally Safety Zone.")
ally_shop = Room("ally shop", "ally base", None, None, None, None, None, None, None,
                 "You are at the shop for allies where you buy items.")
west_ally_open_field = Room("west ally open field", "jungle camp speed west", None, "middle combat field",
                            "west ally safety zone", None, None, None, None,
                            "You are at the west open field where you can fight but it is the outskirts of this place.")
east_ally_open_field = Room("east ally open field", "jungle camp speed east", None, None, "east safety zone", None,
                            None, None, "middle combat field",
                            "You are at the east open field where you can fight but it is the outskirts of this place.")
jungle_camp_mana_west = Room("jungle camp mana west", "jungle camp attack west", "behind the west camps",
                             "middle combat field", "west ally open field", None, None, None, None,
                             "You are at the jungle camp where you can kill a monster for a timed mana regen boost.")
jungle_camp_speed_east = Room("jungle camp speed east", "middle combat field", "behind the east camps",
                              "east ally open field", None, None, None, None, None,
                              "You are at the jungle camp where you can kill a monster for a timed speed boost.")
jungle_camp_attack_west = Room("jungle camp attack west", "jungle camp speed west", "behind the west camps",
                               "middle combat field", "jungle camp mana west", None, None, None, None,
                               "You are at the jungle camp where you can kill a monster for a timed attack boost.")
jungle_camp_attack_east = Room("jungle camp attack east", "jungle camp speed east", "middle combat field",
                               "behind the east camps", "jungle camp mana east", None, None, None, None,
                               "You are at the jungle camp where you can kill a monser for a timed attack boost.")
jungle_camp_mana_east = Room("jungle camp mana east", "jungle camp attack east", "middle combat field",
                             "behind the east camps", "east ally open field", None, None, None, None,
                             "You are at the jungle camp where you can kil a monster for a timed mana boost")
jungle_camp_speed_west = Room("jungle camp speed west", "east enemy open field", "middle combat field,",
                              "behind the east camps", "jungle camp attack west", None, None, None, None,
                              "You are at the west jungle camp where you can kil a monster for a timed speed boost")
behind_the_camps_west = Room("behind the camps west", "jungle camp mana west", None, "jungle camp attack west",
                             "jungle camp speed west", None, None, None, None,
                             "You are behind the jungle camps of the west.")
behind_the_camps_east = Room("behind the camps east", "jungle camp speed east", "jungle camp attack east",
                             None, "jungle camp mana east", None, None, None, None,
                             "You are behind the jungle camps of the east.")
enemy_base = Room(" enemy base", "enemy shop", "east enemy safety zone", "west enemy safety zone", None, None, None,
                  None, None, "You are at the ending point, Enemy Base")
west_enemy_safety_zone = Room("west enemy safety zone", "enemy base", None, "enemy base", "west enemy open field",
                              "enemy portal", None, None, None,
                              "You are at the safety zone for you and your team, West Enemy Safety Zone.")
east_enemy_safety_zone = Room("east enemy safety zone", "enemy base", "enemy portal", "enemy base",
                              "east enemy open field", None, None, None, None,
                              "You are at the safety zone for you and your team, East Enemy Safety Zone.")
enemy_shop = Room("enemy shop", None, None, None, "enemy base", None, None, None, None,
                  "You are at the shop for allies where you buy items.")
west_enemy_open_field = Room("west enemy open field", "west enemy safety zone", "middle combat field", None,
                             "jungle camp speed west", None, None, None, None,
                             "You are at the west open field where you can fight but it is the outskirts of this "
                             "place.")
east_enemy_open_field = Room("east enemy open field", "right enemy safety zone", None, "middle combat field",
                             "jungle camp speed east", None, None, None, None,
                             "You are at the east open field where you can fight but it is the outskirts of this"
                             " place.")
ally_portal = Room("ally portal", "middle combat field", "left ally safety zone", "right ally safety zone", None, None,
                   None, None, None, "You are at your portal. Protect your portal by stopping minions from entering.")
enemy_portal = Room("enemy portal", None, "Right enemy safety zone", "left enemy safety zone", "middle combat field",
                    None, None, None, None, "You are at the enemy portal. Clear a path for your minions to enter the "
                                            "portal.")
middle_of_combat_field = Room("middle combat field", None, "jungle camp attack west", "jungle camp attack east", None,
                              "ally open field east", "ally open field west", "enemy open field east",
                              "enemy open field west", "You are at the combat field. The middle of the map. This is "
                              "where you fight.")

directions = ['north', 'south', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'ne', 'se', 'sw', 'nw']
current_node = ally_base

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
    else:
        print("Command not recognized.")
