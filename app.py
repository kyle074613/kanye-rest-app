from flask import Flask, jsonify
from flask_cors import CORS

import json
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # read JSON file
    with open('db/quotes.json', 'r') as f:
        # run the load method to save to variable
        quotes = json.load(f)

    return jsonify({"quote": random.choice(quotes)}), 200


if __name__ == "__main__":
    app.run()
