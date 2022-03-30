from flask import Flask, request, render_template
from jsonAppend import *


# add method to pass parameters retrieved from addProject.html page to jsonAppend.py to
# append the new project details into the project.json file.
def projectName():
    return request.form['newprojectname']
    #return "name"

def projectDetails():
    return request.form['newprojectdetails']
    #return "Details"

def projectTools():
    return request.form['newprojectTools']
    #return "tools"

def addnewproject():
    return {
                "projectName": projectName(),
                "ProjectDetails": projectDetails(),
                "projectTools": projectTools()
            }

write_json(addnewproject())