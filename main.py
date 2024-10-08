from flask import Flask, jsonify
import random

# Initialize the Flask app
app = Flask(__name__)

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to the Random Number API! Use /random to get a random number.")

# GET endpoint to generate a random number
@app.route("/random", methods=["GET"])
def get_random_number():
    number = random.randint(0, 99)  # Generate a random number between 0 and 99
    return jsonify(random_number=number)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8080)
