from flask import Flask
from flask import render_template

print("test")

app = Flask(__name__)
app.app_context().push()  # for fast updates

print("test git")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)  # automatic starting app
