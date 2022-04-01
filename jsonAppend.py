# Python program to update
# JSON
import json
#from addproject import *
#from addproject import *

# function to add to JSON
def write_json(new_data):
    jsonfile = 'projects.json'
    with open(jsonfile, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["projects"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended
#NewProjectDetailsToBeAdded = {"projectName": "added from",
#      "ProjectDetails": "append.py to",
#      "projectTools": "json file"
#     }

#write_json(NewProjectDetailsToBeAdded)