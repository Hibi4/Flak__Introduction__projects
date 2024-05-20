# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello__world():
    # return "<p>Hello</p>"
    return render_template("index.html")
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/file")
def upload():
    return render_template("file.html")

# Press the green button in the gutter to run the script.

"""if __name__ == '__main__':
    main.run(host=0.0.0.0, debug=True)"""
""",
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == '__main__':
    print_hi('PyCharm') 
"""

# https://www.youtube.com/watch?v=yBDHkveJUf4
# https://flask.palletsprojects.com/en/3.0.x/quickstart/
# jovian.com

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
