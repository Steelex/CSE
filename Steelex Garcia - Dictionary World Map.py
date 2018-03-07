# world_map = {
#     'WESTHOUSE':{
#         'NAME': "West of House",
#         'Description':"You are west of a white house",
#         'PATHS': {
#             'NORTH': 'NORTHHOUSE',
#             'SOUTH': 'SOUTHHOUSE'
#         }
#     },
#     'NORTHOUSE': {
#         'NAME': 'North of House',
#         'PATHS': "Insert Description here",
#         'PATHS': {
#             'SOUTH': 'WESTHOUSE'
#         }
#     },
#     'SOUTHHOUSE': {
#         'NAME': 'South of House',
#         'DESCTRIPTION': 'Insert Description here',
#        'PATHS': {
#             'NORTH': 'WESTHOUSE'
#         }
#     }
# }
world_map = {
    'ALLY BASE': {
        'NAME': "Ally Base",
        'DESCRIPTION': "You are at the starting point, Ally Base",
        'PATHS': {
            'WEST': 'WEST ALLY SAFETY ZONE',
            'EAST': 'EAST ALLY SAFETY ZONE',
            'SOUTH': 'ALLY SHOP'
        }
    },
    'WEST ALLY SAFETY ZONE': {
        'NAME': "West Ally Safety Zone",
        'DESCRIPTION': "You are at the safety zone for you and your team, West Ally Safety Zone.",
        'PATHS': {
            'SOUTH': 'ALLY BASE',
            'NORTH': 'WEST ALLY OPEN FIELD',
            'NE': 'ALLY PORTAL',
            'WEST': 'ALLY BASE'
        }
    },
    'EAST ALLY SAFETY ZONE': {
        'NAME': "East Ally Safety Zone",
        'DESCRITPION': "You are at the safety zone for you and your team, East Ally Safety Zone.",
        'PATHS': {
            'SOUTH': 'ALLY BASE',
            'NORTH': 'EAST ALLY OPEN FIELD',
            'NW': 'ALLY PORTAL',
            'WEST': 'ALLY BASE'
        }
    },
    'ALLY SHOP': {
        'NAME': "Ally Shop",
        'DESCRIPTION': "You are at the shop for allies where you buy items.",
        'PATHS': {
            'NORTH': 'ALLY BASE'
        }
    },
    'WEST ALLY OPEN FIELD': {
        'NAME': "West Ally Open Field",
        'DESCRIPTION': "You are at the west open field where you can fight but it is the outskirts of this place.",
        'PATHS': {
            'SOUTH': 'WEST ALLY SAFETY ZONE',
            'NORTH': 'JUNGLE CAMPLE MANA WEST',
            'EAST': 'MIDDLE COMBAT FIELD'
        }
    },
    'EAST ALLY OPEN FIELD': {
        'NAME': "East Ally Open Field",
        'DESCRITPION': "You are at the east open field where you can fight but it is the outskirts of this place.",
        'PATHS': {
            'NW': 'MIDDLE COMBAT FIELD',
            'SOUTH': 'RIGHT SAFETY ZONE',
            'NORTH': 'JUNGLE CAMP SPEED EAST'
        }
    },
    'JUNGLE CAMP MANA WEST': {
        'NAME': "Jungle Camp Mana West",
        'DESCRIPTION': "You are at the jungle camp where you can kill a monster for a timed mana regen boost.",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP ATTACK WEST',
            'SOUTH': 'WEST ALLY OPEN FIELD ',
            'WEST': 'BEHIND THE CAMPS WEST',
            'EAST': 'MIDDLE COMBAT FIELD'
        }
    },
    'JUNGLE CAMP SPEED EAST': {
        'NAME': "Jungle Camp Speed East",
        'DESCRIPTION': "You are at the jungle camp where you can kill a monster for a timed speed boost.",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP ATTACK EAST',
            'SOUTH': 'EAST ALLY OPEN FIELD ',
            'EAST': 'BEHIND THE CAMPS EAST',
            'WEST': 'MIDDLE COMBAT FIELD'
        }
    },
    'JUNGLE CAMP ATTACK WEST': {
        'NAME': "Jungle Camp Attack West",
        'DESCRIPTION': "You are at the jungle camp where you can kill a monster for a timed attack boost.",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP SPEED WEST',
            'SOUTH': 'JUNGLE CAMP MANA WEST',
            'WEST': 'BEHIND THE CAMPS WEST',
            'EAST': 'MIDDLE COMBAT FIELD'
        }
    },
    'JUNGLE CAMP ATTACK EAST': {
        'NAME': "Jungle Camp Attack East",
        'DESCRIPTION': "You are at the jungle camp where you can kill a monser for a timed attack boost.",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP SPEED EAST',
            'SOUTH': 'JUNGLE CAMP MANA EAST',
            'EAST': 'BEHIND THE CAMPS EAST',
            'WEST': 'MIDDLE COMBAT FIELD'
        }
    },
    'JUNGLE CAMP MANA EAST': {
        'NAME': "Jungle Camp Mana East",
        'DESCRIPTION': "You are at the  east jungle camp where you can kil a monster for a timed mana boost",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP ATTACK EAST',
            'SOUTH': 'EAST ALLY OPEN FIELD ',
            'EAST': 'BEHIND THE CAMPS EAST',
            'WEST': 'MIDDLE COMBAT FIELD'
        }
    },
    'JUNGLE CAMP SPEED WEST': {
        'NAME': "Jungle Camp Mana East",
        'DESCRIPTION': "You are at the west jungle camp where you can kil a monster for a timed speed boost",
        'PATHS': {
            'SOUTH': 'JUNGLE CAMP ATTACK EAST',
            'NORTH': 'EAST ENEMY OPEN FIELD ',
            'EAST': 'BEHIND THE CAMPS EAST',
            'WEST': 'MIDDLE COMBAT FIELD'
        }
    },
    'BEHIND CAMPS WEST': {
        'NAME': "Behind Camps West",
        'DESCRIPTION': "You are behind the jungle camps of the west.",
        'PATHS': {
            'NORTH': 'JUNGLE CAMP MANA WEST',
            'SOUTH': 'JUNGLE CAMP SPEED WEST',
            'EAST': 'JUNGLE CAMP ATTACK WEST'
        }
    },
    'BEHIND CAMPS EAST': {
        'NAME': "Behind Camps East",
        'DESCRIPTION': "You are behind the jungle camps of the east.",
        'PATHS': {
            'SOUTH': 'JUNGLE CAMP MANA EAST',
            'NORTH': 'JUNGLE CAMP SPEED EAST',
            'WEST': 'JUNGLE CAMP ATTACK EAST'
        }
    },
    'ENEMY BASE': {
        'NAME': "Enemy Base",
        'DESCRIPTION': "You are at the ending point, Enemy Base",
        'PATHS': {
            'EAST': 'WEST ENEMY SAFETY ZONE',
            'WEST': 'EAST ENEMY SAFETY ZONE',
            'NORTH': 'ENEMY SHOP'
        }
    },
    'WEST ENEMY SAFETY ZONE': {
        'NAME': "West Enemy Safety Zone",
        'DESCRIPTION': "You are at the safety zone for you and your team, West Enemy Safety Zone.",
        'PATHS': {
            'NORTH': 'ENEMY BASE',
            'SOUTH': 'WEST ENEMY OPEN FIELD',
            'SE': 'ENEMY PORTAL',
            'EAST': 'ENEMY BASE'
        }
    },
    'EAST ENEMY SAFETY ZONE': {
        'NAME': "East Enemy Safety Zone",
        'DESCRITPION': "You are at the safety zone for you and your team, East Enemy Safety Zone.",
        'PATHS': {
            'NORTH': 'ENEMY BASE',
            'SOUTH': 'EAST ENEMY OPEN FIELD',
            'WEST': 'ENEMY PORTAL',
            'EAST': 'ENEMY BASE'
        }
    },
    'ENEMY SHOP': {
        'NAME': "Enemy Shop",
        'DESCRIPTION': "You are at the shop for allies where you buy items.",
        'PATHS': {
            'SOUTH': 'ENEMY BASE'
        }
    },
    'WEST ENEMY OPEN FIELD': {
        'NAME': "West Enemy Open Field",
        'DESCRIPTION': "You are at the west open field where you can fight but it is the outskirts of this place.",
        'PATHS': {
            'NORTH': 'WEST ENEMY SAFETY ZONE',
            'SOUTH': 'JUNGLE CAMPLE SPEED WEST',
            'WEST': 'MIDDLE COMBAT FIELD'
        }
    },
    'EAST ENEMY OPEN FIELD': {
        'NAME': "East Enemy Open Field",
        'DESCRITPION': "You are at the east open field where you can fight but it is the outskirts of this place.",
        'PATHS': {
            'EAST': 'MIDDLE COMBAT FIELD',
            'NORTH': 'RIGHT ENEMY SAFETY ZONE',
            'SOUTH': 'JUNGLE CAMP SPEED EAST'
        }
    },
    'ALLY PORTAL': {
        'NAME': "Ally Portal",
        'DESCRIPTION': "You are at your portal. Protect your portal by stopping minions from entering.",
        'PATHS': {
            'EAST': 'RIGHT ALLY SAFETY ZONE',
            'WEST': 'LEFT ALLY SAFETY ZONE',
    '       NORTH': 'MIDDLE COMBAT FIELD'
        }
    },
    'ENEMY PORTAL': {
        'NAME': "Enemy Portal",
        'DESCRIPTION': "You are at the enemy portal. Clear a path for your minions to enter the portal.",
        'Paths': {
            'WEST': 'RIGHT ENEMY SAFETY ZONE',
            'EAST': 'LEFT ENEMY SAFETY ZONE',
            'SOUTH': 'MIDDLE COMBAT FIELD'
        }
    },
    'MIDDLE OF COMBAT FIELD': {
    'NAME': "Combat Field",
    'DESCRIPTION': "You are at the combat field. The middle of the map. This is where you fight.",
    'PATHS': {
        '    SW': 'ALLY OPEN FIELD WEST',
            'SE': 'ALLY OPEN FIELD EAST',
            'NE': 'ENEMY OPEN FIELD EAST',
            'NW': 'ENEMY OPEN FIELD WEST',
            'WEST': 'JUNGLE CAMP ATTACK WEST',
            'EAST': 'JUNGLE CAMP ATTACK EAST'
        }
    }
}

current_node = world_map['ALLY BASE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NW', 'NE', 'SW', 'SE']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        name_of_node = current_node['PATHS'][command]
        current_node = world_map[name_of_node]
    if command == ('NORTH'):
        print("You Moved")
    else:
        print('Command not Recognized')



