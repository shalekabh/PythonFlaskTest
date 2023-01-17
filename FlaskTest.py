# Import rescoursces from flask
from flask import Flask, redirect, url_for, render_template, request
# create variable for our application
app = Flask (__name__)
# Create a weblink page using @ and .route our route is /
# Pass flask information from html template to the return "content" is passed from flask to html
# You can add more to the html template and pass it back to python (return)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new_index.html")
#GET/POST get is when you type in unsecure urls it will send information to the web browser and get the webpae back
#GET/POST post is a secure way to do GET because post is encrypted
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
#Forms are how we send information to a website (check html pages)
@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome to Black-Heaven {usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)