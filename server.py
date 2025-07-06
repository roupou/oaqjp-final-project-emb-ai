from flask import Flask, request, render_template
from emotion_detection import em

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # index.html must be in the templates folder

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    text = request.form['text']  # input field name="text" in the HTML

    # Get result from your module
    result = emotion_predictor(text)

    # Extract emotions
    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant = result.get("dominant_emotion", "unknown")

    # Format output
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."
    )

    return response
