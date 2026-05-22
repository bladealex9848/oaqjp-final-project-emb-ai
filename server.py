"""
Flask server for the Emotion Detection application.
Provides an endpoint to analyze emotions in text using the Watson NLP library.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint to receive text, run emotion detection, and return a formatted string response.
    Handles blank or invalid input errors by displaying an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    # Analyze emotion
    result = emotion_detector(text_to_analyze)
    # Handle case where dominant_emotion is None (invalid/blank input)
    if result["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"
    # Format response string
    response_msg = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} y "
        f"'sadness': {result['sadness']}. "
        f"La emoción dominante es <b>{result['dominant_emotion']}</b>."
    )
    return response_msg

@app.route("/")
def render_index():
    """
    Renders the index.html page as the main UI.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
