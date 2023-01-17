# Import rescoursces from flask
from flask import Flask, redirect, url_for, render_template
# create boilerplate for our code
app = Flask (__name__)
# Create a weblink page using @ and .route our route is /
# Define our home page function and message in bold header
@app.route("/")
def home():
    return "<h1>I did it</h1>"
# Create a weblink the user can input a variable use <> to pullt it to the definition 
# Define funtion of user()
# Return it with the funtion key "f" to activate the function on return
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# Create a restricted weblink to admin
# Define admin funtion
# Use imported rescources redirect and url_for to redirect back to home page if admin route is input
# To redirect to a different page like user we would need to also create the path for (name) the code /
# to replace "home" is : ("user", name="Admin!") this will create a path for the argument (name)
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="You Are A Poo!"))


if __name__ == "__main__":
    app.run()