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
        <!-- create your form here -->
        <form action-"/encrypt" method="post">
            <label for="rot">
                Rotate by:
                <input type="text" name="rot" />
            </label>
            <textarea name="text" rows="10" cols="30"></textarea>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web Caesar</title>
    </head>
    <body>
"""

page_footer = """
</body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(rota, orig_text):
    rota = int(request.form['rot'])
    orig_text = str(request.form['text'])
    rotated_text = rotate_string(orig_text, rota)
    rotated_text_element = "<h1>" + rotated_text + "</h1>"
    content = page_header + rotated_text_element + page_footer
    return content


app.run()
