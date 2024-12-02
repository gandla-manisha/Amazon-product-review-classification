import joblib
import pickle  # Assuming you saved your model using joblib

# Load the trained model (SVM or Naive Bayes)
with open('sentiment_analyser.pkl', 'rb') as f:  # Open the file in 'rb' mode
    model = pickle.load(f)  # Load the model

with open('vectorizer.pkl', 'rb') as f:  # Open the vectorizer file in 'rb' mode
    vectorizer = pickle.load(f)  # Load the vectorizer

# Load the trained model (SVM or Naive Bayes)
  # Path to your saved vectorizer

def predict_sentiment(reviews):
    """
    Predict the sentiment for a list of reviews.
    """
    # Transform reviews into model-compatible format
    X = vectorizer.transform(reviews)
    
    # Predict sentiment (0: Negative, 1: Neutral, 2: Positive)
    predictions = model.predict(X)
    
    # Map predictions to sentiment
    sentiments = ['Negative', 'Neutral', 'Positive']
    final_sentiment = sentiments[max(set(predictions), key=predictions.tolist().count)]  # Majority sentiment
    
    return final_sentiment