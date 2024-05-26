# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

""" return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS """


@app.route('/file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'File {filename} uploaded successfully!'
        else:
            return "This file extension is not allowed"

    return 'File upload failed'

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
