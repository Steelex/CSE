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
    'WEST ALLY SAFETY ZONE':{
        'NAME': "West Ally Safety Zone",
        'DESCRIPTION': "You are at the safety zone for you and your team, West Ally Safety Zone.",
        'PATHS':{
            'SOUTH': 'ALLY BASE',
            'NORTH': 'WEST ALLY OPEN FIELD',
            'NE': 'ALLY PORTAL',
            'WEST': 'ALLY BASE'
        }
    },
    'EAST ALLY SAFETY ZONE':{
        'NAME': "East Ally Safety Zone",
        'DESCRITPION': "You are at the safety zone for you and your team, East Ally Safety Zone.",
        'PATHS': {
            'SOUTH': 'ALLY BASE',
            'NORTH': 'EAST ALLY OPEN FIELD',
            'NW': 'ALLY PORTAL',
            'WEST': 'ALLY BASE'
        }
    },
    'ALLY SHOP':{
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
            'NORTH': 'JUNGLE CAMPLE SPEED',
            'WEST: ': ''
        }
    }
}

current_node = world_map['ALLY BASE']
directions = [ 'NORTH', 'SOUTH', 'EAST', 'WEST', 'NW', 'NE', 'SW', 'SE']

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
