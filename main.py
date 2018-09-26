from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
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
      <form action="/" method="post">
      <label for="rotate">Rotate by</label>
      <input id="rotate" type="number" name="rot" value="0" />
      <br>
      <textarea name="text" rows="4" cols="50"></textarea>
      <input type="submit" />
      </form>
    </body>
</html>    
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    rot_text = str(request.form["text"])
    encrypt_text = rotate_string(rot_text, rot)
    return form(encrypt_text)
    
app.run()