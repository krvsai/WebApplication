# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from flask import render_template
from flask import *
#from jsonif import *
#from request import *
from flask_restful import *
import addproject
import jsonAppend
import json
import logging
#import jsonRead, addproject, projects, jsonWrite, jsonAppend, json
#from addproject import *

logging.basicConfig(level=logging.DEBUG)

# using flask_restful
# creating the flask app
app = Flask(__name__, template_folder='templates')
# creating an API object
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shortintro")
def shortintro():
    return render_template("shortintro.html")


@app.route("/skillset")
def skillset():
    return render_template("skillset.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/projects")
def projects():
    if request.method == 'GET':
        # Opening JSON file
        f = open('projects.json')
        # returns JSON object as a dictionary
        projectslist = json.load(f)
        app.logger.info("Projectslit:  {}".format(projectslist))
        f.close()
    return render_template("projects.html", projectslist = projectslist)


@app.route("/addProject", methods=('POST', 'GET'))
def addProject():
    if request.method == 'POST':
        jsonAppend.write_json(addproject.addnewproject())
        return redirect(url_for('successful'))
    return render_template("addProject.html")


@app.route("/successful")
def successful():
    return render_template("successful.html")


@app.route("/contactme")
def contactme():
    return render_template("contactme.html")


if __name__ == "__main__":
    app.run(debug=True)
    #app.debug=True