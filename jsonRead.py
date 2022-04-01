import json

# Opening JSON file
f = open('projects.json')

# returns JSON object as
# a dictionary
projects = json.load(f)

# Iterating through the json
# list
for i in projects['projects']:
    print(i)  # prints in the console

# Closing file
f.close()
