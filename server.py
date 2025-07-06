from flask import Flask, request, render_template
from final_project import emotion_detection  # assumes emotion_detection.py is inside final_project/

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text = request.form['text']  # input field name="text" in the HTML

    # Call your actual emotion function
    result = emotion_detection.emotion_detector(text)

    # Extract emotions
    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant = result.get("dominant_emotion", "unknown")

    # Format the response
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."
    )

    return response

if __name__ == '__main__':
    app.run(debug=True)
