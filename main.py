from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    kanye_url = "https://api.kanye.rest"
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    advice_url = "https://api.adviceslip.com/advice"
    trivia_url = "http://numbersapi.com/random/trivia"

    kanye_data = requests.get(kanye_url).json()
    joke_data = requests.get(joke_url).json()
    advice_data = requests.get(advice_url).json()
    trivia_data = requests.get(trivia_url).text

    quote = kanye_data["quote"]
    joke = f"{joke_data['setup']} - {joke_data['punchline']}"
    advice = advice_data["slip"]["advice"]
    trivia = trivia_data

    user_quote = request.args.get("user_quote", "")

    return render_template("index.html", quote=quote, joke=joke, advice=advice, trivia=trivia, user_quote=user_quote)

@app.route("/api/data")
def get_data():
    kanye_url = "https://api.kanye.rest"
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    advice_url = "https://api.adviceslip.com/advice"
    trivia_url = "http://numbersapi.com/random/trivia"

    kanye_data = requests.get(kanye_url).json()
    joke_data = requests.get(joke_url).json()
    advice_data = requests.get(advice_url).json()
    trivia_data = requests.get(trivia_url).text

    quote = kanye_data["quote"]
    joke = f"{joke_data['setup']} - {joke_data['punchline']}"
    advice = advice_data["slip"]["advice"]
    trivia = trivia_data

    return jsonify(quote=quote, joke=joke, advice=advice, trivia=trivia)

@app.route("/submit_quote", methods=["POST"])
def submit_quote():
    user_quote = request.form["user_quote"]
    return render_template("index.html", user_quote=user_quote)
