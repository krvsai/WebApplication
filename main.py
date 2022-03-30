# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, jsonify, request
from flask import render_template
from flask_restful import Resource, Api
#import jsonRead, addproject, projects, jsonWrite, jsonAppend, json

# using flask_restful
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/shortInto")
def shortInto():
    return render_template("shortInto.html")
@app.route("/skillset")
def skillset():
    return render_template("skillset.html")
@app.route("/education")
def education():
    return render_template("education.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")
@app.route("/addProject")
def addProject():
    return render_template("addProject.html")

if __name__ == "__main__":
    app.run(debug=True)