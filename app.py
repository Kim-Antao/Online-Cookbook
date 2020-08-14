import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'CookBook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
"""
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
"""
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("index.html",recipes=mongo.db.recipes.find())

if __name__=="__main__":
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')),
            debug=True)
 