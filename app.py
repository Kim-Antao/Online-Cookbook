import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/new_recipe")
def new_recipe():
    return render_template("new_recipe.html", cuisines=mongo.db.cuisine.find())


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one({
        "title": request.form.get("title"),
        "image_src": request.form.get("image_src"),
        "prep_time": request.form.get("prep_time"),
        "cook_time": request.form.get("cook_time"),
        "serving": request.form.get("serving"),
        "calories": request.form.get("calories"),
        "cuisine": request.form.get("cuisine"),
        "type": request.form.get("type"),
        "ingredients": request.form.getlist("ingredients[]"),
        "instructions": request.form.getlist("instructions[]")})
    return redirect(url_for("index_page"))


@app.route("/list_cuisines")
def list_cuisines():
    return render_template("search.html", cuisines=mongo.db.cuisine.find())


@app.route("/list_recipes")
def list_recipes():
    recipes = mongo.db.recipe.fine({"cuisine": "indian"})
    return render_template("search.html", recipes)


@app.route("/view_recipe")
def view_recipe():
    recipe_id = "5f316631b183403e0d6d8bb6"
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view.html", recipe=the_recipe)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
            else:
                # password does not match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registered Successfully")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
