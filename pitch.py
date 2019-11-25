from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def home():

    return "<h1>Home page</h1>"

@app.route("/About")
def about():

    return "About"

if __name__ == "__main__":
    app.run(debug=True)