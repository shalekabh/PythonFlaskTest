# Import rescoursces from flask
from flask import Flask, redirect, url_for, render_template
# create variable for our application (boilerplate)
app = Flask (__name__)
# Create a weblink page using @ and .route our route is /
# Pass flask information from html template to the return "content" is passed from flask to html
# You can add more to the html template and pass it back to python (return)
# You can write code in your html template using {%%} including loops this will show on the weblink
# I attached a list to my alias "content" and added "content" to my for loop in the html template
@app.route("/")
def home():
    return render_template("index_two.html", content=["You", "think", "i'm", "sexy!"])

if __name__ == "__main__":
    app.run()