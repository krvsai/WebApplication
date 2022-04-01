from flask import Flask, request, render_template
from jsonAppend import *


# add method to pass parameters retrieved from addProject.html page to jsonAppend.py to
# append the new project details into the project.json file.
def projectname():
    return request.form['projectName']
    #return "name"


def projectdetails():
    return request.form['projectDetails']
    #return "Details"


def projecttools():
    return request.form['projectTools']
    #return "tools"


def addnewproject():
    return {
                "projectName": projectname(),
                "ProjectDetails": projectdetails(),
                "projectTools": projecttools()
            }


