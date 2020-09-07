import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
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


@app.route("/insert_recipe", methods=["POST", "GET"])
def insert_recipe():
    if request.method == "POST":
        recipe = mongo.db.recipes

        new_recipe = recipe.insert({
            "title": request.form.get("title"),
            "image_src": request.form.get("image_src"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "calories": request.form.get("calories"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("type"),
            "ingredients": request.form.getlist("ingredients[]"),
            "instructions": request.form.getlist("instructions[]"),
            "username": session["user"]})
        tool = mongo.db.tools
        
        tool.insert_one({
            "name": request.form.getlist("name[]"),
            "link": request.form.getlist("link[]"),
            "recipe_id": new_recipe})
        return redirect(url_for("index_page"))

    return render_template("new_recipe.html", cuisines=mongo.db.cuisine.find())


@app.route("/display_message")
def display_message():
    flash("Please Login to add a recipe", "info")
    return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        clicked = request.form.get("cuisine")
        recipes = mongo.db.recipes.find({"cuisine": clicked})
        recipe_count = recipes.count()
        if (recipe_count != 0):
            return render_template("search.html", clicked=clicked, cuisines=mongo.db.cuisine.find(), recipes=recipes)
        else:
            flash("Be The First One To Add A Recipe", "message")
            return render_template("search.html", clicked=clicked, cuisines=mongo.db.cuisine.find(), recipes=recipes)

    recipes = mongo.db.recipes.find({"cuisine": "Indian"})
    clicked = "Indian"
    return render_template("search.html", clicked=clicked, cuisines=mongo.db.cuisine.find(), recipes=recipes)


@app.route("/view_recipe/<id>")
def view_recipe(id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    tools = mongo.db.tools.find({'recipe_id': ObjectId(id)})
    return render_template("view.html", recipe=the_recipe, tools=tools)


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    # get the sessions user's username from the db
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = recipe['username']
    
    if session["user"] == username:
        
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        mongo.db.tools.remove({"recipe_id": ObjectId(recipe_id)})
        return redirect(url_for("search"))
    else:
        flash("You Cannot Delete Recipes Added By Another User", "error")
        return redirect(url_for("search"))


@app.route("/display_message1")
def display_message1():
    flash("Please Login to Delete a recipe", "info")
    return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipe = mongo.db.recipes
        recipe.update_one({"_id": ObjectId(recipe_id)},
        {"$set" : {
            "title": request.form.get("title"),
            "image_src": request.form.get("image_src"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "calories": request.form.get("calories"),
            "cuisine": request.form.get("cuisine"),
            "type": request.form.get("type"),
            "ingredients": request.form.getlist("ingredients[]"),
            "instructions": request.form.getlist("instructions[]"),
            "username": session["user"]
        }})
        tools = mongo.db.tools
        tools.update_one({"recipe_id": ObjectId(recipe_id)},
        {"$set" : {
            "name": request.form.getlist("name[]"),
            "link": request.form.getlist("link[]"),
            "recipe_id": ObjectId(recipe_id)
        }})

        return redirect(url_for("view_recipe", id=recipe_id))
    # get the sessions user's username from the db
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = recipe['username']
    tools = mongo.db.tools.find({"recipe_id": ObjectId(recipe_id)})
    if session["user"] == username:
        cuisines = mongo.db.cuisine.find()
        return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines, tools=tools)
    else:
        flash("You Cannot Edit Recipes Added By Another User", "error")
        return redirect(url_for("search"))


@app.route("/display_message2")
def display_message2():
    flash("Please Login to Edit a recipe", "info")
    return redirect(url_for("login"))


@app.route("/buy")
def buy():
    tools = mongo.db.tools.find()
    return render_template("buy.html", tools=tools)


@app.route("/dashboard")
def dashboard():
    count_user = mongo.db.users.count()
    count_recipe = mongo.db.recipes.count()
    return render_template("dashboard.html", count_user=count_user, count_recipe=count_recipe)


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
                flash("Welcome {}".format(
                    request.form.get("username")), "message")
                return redirect(url_for(
                    "index_page", username=session["user"]))
            else:
                # password does not match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registered Successfully", "message")
        return redirect(url_for("index_page"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    flash("You have logged out successfully", "message")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
