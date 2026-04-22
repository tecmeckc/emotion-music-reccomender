from flask import Flask, render_template, request
from youtube_api import get_videos_by_mood

app = Flask(__name__)

mood_keywords = {
    "happy": ["happy", "joy", "excited", "great", "good", "amazing", "awesome"],
    "sad": ["sad", "low", "down", "depressed", "unhappy", "upset", "heartbroken"],
    "angry": ["angry", "mad", "furious", "annoyed", "frustrated"],
    "romantic": ["love", "romantic", "crush", "relationship"],
    "calm": ["calm", "peaceful", "relaxed", "chill"],
    "energetic": ["energy", "party", "dance", "hyped"]
}

def detect_mood(text):
    text = text.lower()

    if "not happy" in text or "not good" in text:
        return "sad"

    mood_score = {mood: 0 for mood in mood_keywords}

    for mood, words in mood_keywords.items():
        for word in words:
            if word in text:
                mood_score[mood] += 1

    detected_mood = max(mood_score, key=mood_score.get)

    if mood_score[detected_mood] == 0:
        return "neutral"

    return detected_mood


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    user_text = request.form["mood_text"]

    mood = detect_mood(user_text)

    videos = get_videos_by_mood(mood)

    return render_template(
        "result.html",
        mood=mood,
        user_text=user_text,
        videos=videos
    )


if __name__ == "__main__":
    app.run(debug=True)