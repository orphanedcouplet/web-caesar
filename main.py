from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method="post">
            <label for="rot">
                Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <label>
                    <textarea name="text">{0}</textarea>
            </label>
            <input type="submit" value="Submit Query" />
        </form>
    </body>    
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rota = int(request.form['rot'])
    orig_text = str(request.form['text'])
    rotated_text = rotate_string(orig_text, rota)
    return form.format(rotated_text)


app.run()
