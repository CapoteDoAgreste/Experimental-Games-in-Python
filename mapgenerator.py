import json

# create a array with the width height
x = 52
y = 52
new_map_layout = [[0]*x for _ in range(y)]


# crete and write the json file with the map dimension what do you need
with open('new_map_layout.json', 'w') as f:
    json.dump(new_map_layout, f)
