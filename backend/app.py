from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

# Load exercises.json
with open("data/exercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

@app.route("/recommend", methods=["GET"])
def recommend():
    goal = request.args.get("goal", "").lower()

    # Simple filtering logic
    if goal == "weight loss":
        filtered = [e for e in exercises if "cardio" in e["category"].lower()]
    elif goal == "muscle gain":
        filtered = [e for e in exercises if "strength" in e["category"].lower()]
    elif goal == "beginner":
        filtered = [e for e in exercises if e.get("level", "").lower() == "beginner"]
    else:
        filtered = exercises  # default: return all

    # Random 3 recommendations
    recommendations = random.sample(filtered, min(3, len(filtered)))
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
