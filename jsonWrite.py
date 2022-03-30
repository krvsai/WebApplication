# Python program to write JSON to a file


import json

# Data to be written
dictionary = {
    "projects": [
        {
      "projectName": "Freshly",
      "ProjectDetails": "write project details to ",
      "projectTools": "json file"
        }
    ]
}

# Serializing json
json_object = json.dumps(dictionary, indent=1)

# Writing to sample.json
with open("projects.json", "w") as outfile:
    outfile.write(json_object)