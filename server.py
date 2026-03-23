from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """Handle emotion detection requests."""
    text = request.args.get("textToAnalyze")

    if not text:
        return jsonify({"error": "Invalid input"}), 400

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text"}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
