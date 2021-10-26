import os


# Python program to read
# json file


import json

def parse_soundboard():
    if os.path.isfile('./sounds/soundboard.json'):
        pass
    else:
        os.popen('wget -P sounds/ https://www.spranga.xyz/soundboard.json').read()
    #os.system('wget -P sounds/ https://www.spranga.xyz/soundboard.json')
    # Opening JSON file
    f = open('sounds/soundboard.json',)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    all_data = {}
    for i in data['files']:
        all_data[i['name']] = i

    # Closing file
    f.close()
    return all_data
