"""Flask server for emotion detection web application."""
from flask import Flask, request, render_template
from final_project import emotion_detection

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle emotion detection from text input."""
    text = request.form['text']
    result = emotion_detection.emotion_detector(text)

    # Handle None case or error
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Extract emotions
    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant = result.get("dominant_emotion", "unknown")

    # Format response
    response = (
        f"For the given statement, the system response is:\n"
        f"• anger: {anger}\n"
        f"• disgust: {disgust}\n"
        f"• fear: {fear}\n"
        f"• joy: {joy}\n"
        f"• sadness: {sadness}\n"
        f"The dominant emotion is: {dominant}."
    )

    return response

if __name__ == '__main__':
    app.run(debug=True)
