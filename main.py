from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method='POST' name="hi">
            <label for="rot">
                Rotate by:<input type="text" id="rot" name="rot" value="0"/><br>
                <input type="textarea" id="text" name="text"/><br>
                <input type="submit"/>
            </label>
        </form>

    </body>
</html>"""

@app.route("/")
def index():
    content = form
    return content

@app.route("/caesar", methods=['POST'])
def caesar():
    return request.form['text']

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    return "<h1>{}</h1>".format(rotate_string(text, rot))

app.run()