# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
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