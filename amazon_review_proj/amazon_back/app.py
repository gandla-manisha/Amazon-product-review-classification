from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend

# Load the trained model and vectorizer
try:
    with open("sentiment_analyser.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading sentiment model: {str(e)}")
    exit()

try:
    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    print("Vectorizer loaded successfully.")
except Exception as e:
    print(f"Error loading vectorizer: {str(e)}")
    exit()

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json  # Input data from frontend
    reviews = data.get("reviews", [])

    if not reviews:
        return jsonify({"error": "No reviews provided"}), 400

    try:
        # Transform reviews using the vectorizer
        reviews_transformed = vectorizer.transform(reviews)

        # Predict sentiments
        predictions = model.predict(reviews_transformed)
        sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}  # Example mapping
        labeled_predictions = [sentiment_map.get(pred, "Unknown") for pred in predictions]
        # Create a summary of the results
        summary = {
            "positive": sum(1 for sentiment in predictions if sentiment == "Positive"),
            "negative": sum(1 for sentiment in predictions if sentiment == "Negative"),
            "neutral": sum(1 for sentiment in predictions if sentiment == "Neutral"),
        }

        # Identify the most common sentiment
        max_sentiment = max(summary, key=summary.get)

        return jsonify({
            "results": labeled_predictions,
            "summary": summary,
            "max_sentiment": max_sentiment
        })

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
