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
    current_node = globals() [getattr(self, direction)]


# Initialize Room
ally_base = Room("ally base", None, "west ally safety zone", "east ally safety zone", "ally shop", None, None, None,
                 None, "You are at the starting point")
west_ally_safety_zone = Room("west ally safety zone", "west ally open field", None, "ally base", "ally base", None,
                             None, "ally portal", None)
east_ally_safety_zone = Room("east ally safety zone", "east ally open field", "ally base", None, None, "ally base",
                             None, None, "ally portal", None)
ally_shop = Room("ally shop", "ally base", None, None, None, None, None, None, None)
west_ally_open_field = Room("west ally open field", "jungle camp speed west", None, "middle combat field",
                            "west ally safety zone", None, None, None, None)
east_ally_open_field = Room("east ally open field", "jungle camp speed east", None, None, "east safety zone", None,
                            None, None, "middle combat field")
jungle_camp_mana_west = Room("jungle camp mana west", "jungle camp attack west", "behind the west camps",
                             "middle combat field", "west ally open field", None, None, None, None)
jungle_camp_speed_east = Room("jungle camp speed east", "middle combat field", "behind the east camps",
                              "east ally open field", None, None, None, None)
jungle_camp_attack_west = Room("jungle camp attack west", "jungle camp speed west", "behind the west camps",
                               "middle combat field", "jungle camp mana west",None, None, None, None)
jungle_camp_attack_east = Room("jungle camp attack east", "jungle camp speed east", "middle combat field",
                               "behind the east camps", "jungle camp mana east", None, None, None, None)
jungle_camp_mana_east = Room("jungle camp mana east", "jungle camp attack east", "middle combat field",
                             "behind the east camps", "east ally open field", None, None, None, None)
jungle_camp_speed_west = Room("jungle camp speed west", "east enemy open field", "middle combat field,",
                              "behind the east camps", "jungle camp attack west", None, None, None, None)
behind_the_camps_west = Room("behind the camps west", "jungle camp mana west", None, "jungle camp attack west",
                             "jungle camp speed west", None, None, None, None)
behind_the_camps_east = Room("behind the camps east", "jungle camp speed east", "jungle camp attack east",
                             None, "jungle camp mana east", None, None, None, None)
enemy_base = Room(" enemy base", "enemy shop", "east enemy safety zone", "west enemy safety zone", None, None, None,
                None, None)
west_enemy_safety_zone = Room("west enemy safety zone", "enemy base", None, "enemy base", "west enemy open field",
                              "enemy portal", None, None, None)
east_enemy_safety_zone = Room("east enemy safety zone", "enemy base", "enemy portal", "enemy base",
                              "east enemy open field", None, None, None, None)
enemy_shop = Room("enemy shop", None, None, None, "enemy base", None, None, None, None)
west_enemy_open_field = Room("west enemy open field", "west enemy safety zone", "middle combat field", None,
                             "jungle camp speed west", None, None, None, None)
east_enemy_open_field = Room("east enemy open field", "right enemy safety zone", None, "middle combat field",
                             "jungle camp speed east", None, None, None, None)
ally_portal = Room("ally portal", "middle combat field", "left ally safety zone", "right ally safety zone", None, None,
                   None, None, None)
enemy_portal = Room("enemy portal", "")
