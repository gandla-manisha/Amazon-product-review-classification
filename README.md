# Amazon-product-review-classification
Amazon Product Review Sentiment Classification
This project provides a web application for classifying Amazon product reviews into sentiments: Positive, Negative, or Neutral. The app uses a Flask backend for sentiment analysis and a visually appealing frontend to display results in a table format.

Features
Accepts multiple Amazon product reviews as input.
Classifies each review as Positive, Negative, or Neutral.
Displays results in a table format with Review and Sentiment columns.
Highlights the most frequent sentiment among the provided reviews.

Requirements
Python Dependencies
Ensure the following Python packages are installed:
Flask
Flask-CORS
scikit-learn
pickle (for loading pre-trained model)
numpy
Install these dependencies using:


pip install -r requirements.txt
Requirements File
Create a requirements.txt file with the following content:

Flask
Flask-CORS
scikit-learn
numpy
How to Run
Prerequisites
Python Environment: Ensure you have Python 3.7 or above installed.
Dependencies: Install the required Python libraries:

pip install -r requirements.txt
Files Required
sentiment_analyser.pkl: The trained sentiment classification model.
vectorizer.pkl: The vectorizer used to preprocess input text.
app.py: The Flask backend server script.
Frontend files (e.g., index.html, style.css).
Steps to Run
Backend Setup

Place the sentiment_analyser.pkl and vectorizer.pkl files in the same directory as app.py.
Run the Flask server:
python app.py
The server will start at http://127.0.0.1:5000.
Frontend Access

Open the frontend HTML file (index.html) in a browser.
Enter or paste the reviews into the input box.
Click the Analyze button to view the results.
API Endpoint
POST /analyze
Request Format:

json

{
    "reviews": [
        "This product is amazing!",
        "Not worth the price."
    ]
}
Response Format:

json
Copy code
{
    "results_table": [
        {"review": "This product is amazing!", "sentiment": "Positive"},
        {"review": "Not worth the price.", "sentiment": "Negative"}
    ],
    "summary": {
        "positive": 1,
        "negative": 1,
        "neutral": 0
    }
}
Example Workflow
Enter reviews (one per line) in the input box.
Click Analyze.
View results in the table:
Review: Displays the original review text.
Sentiment: Displays the classification result (Positive, Negative, Neutral).
The most frequent sentiment is shown below the table.
Project Files
Backend:
app.py: Flask API logic.
sentiment_analyser.pkl: Trained sentiment analysis model.
vectorizer.pkl: Preprocessor for input text.
Frontend:
index.html: User interface for input and result display.
style.css: Styling for the web page.
script.js (optional): Handles user interactions and API calls.
[ML proj.pptx](https://github.com/user-attachments/files/17978983/ML.proj.pptx)

License
This project is for educational purposes and can be freely modified.




