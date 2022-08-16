from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import json
import random
import googletrans
import tools.mongo_tools as mongo
import tools.sql_tools as sql

app = Flask(__name__)

# GET: render markdown
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

# Get a list of all days with tweets
@app.route("/dates/")
def all_lines ():
    return jsonify(sql.get_days())

# Get everything FROM a particular day: SQL
@app.route("/date/<date>/")
def daily_tweets (date):
    return jsonify(sql.get_everything_from_day(date))

# Get one tweet FROM a day AND translate it:   
@app.route("/translate/<date>") #add ?language=ES or whatever language we want to the end of the route
def one_random_language (date):
    tweets = sql.get_everything_from_day(date)
    tweet = random.choice(tweets)
    language = request.args["language"]
    trans = googletrans.Translator()
    result = trans.translate(tweet["tweet"], dest=language)
    tweet["tweet"] = result.text
    return tweet

## POST
@app.route("/newtweet/", methods=["POST"])
def insert_message():
    date = request.form.get("date")
    tweet = request.form.get("tweet")
    language = request.form.get("language")
    return sql.new_message(date, tweet, language)

@app.route("/deleteday/", methods=["POST"])
def delete_day():
    date = request.form.get("date")
    return sql.erase_day(date)

app.run(debug=True)

