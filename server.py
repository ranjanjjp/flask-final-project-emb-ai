"""Flask app for emotion detection using Watson NLP API."""

from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detect_emotion():
    """Route to detect emotions from provided text."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return jsonify(response)

@app.route("/")
def render_index_page():
    """Renders the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
