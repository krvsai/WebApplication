import json


def json2object():
    f = open('projects.json')
    # returns JSON object as
    # a dictionary
    g = {"p":[{"1": "yes"}, {"2": "no"}, {"3": "Maybe"}]}
    projectslist = json.loads(g)
    print(projectslist)


def json2string():
    y = json.dumps('projects.json')
    print(y)
