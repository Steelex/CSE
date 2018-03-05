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
jungle_campe_attack_west = Room()
