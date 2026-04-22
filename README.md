# 🎧 Emotion-Aware Music Recommendation System

An intelligent web application that detects user emotions from text input and recommends music accordingly using a rule-based NLP approach and YouTube API integration.

---

## 🚀 Features

- 🎭 Emotion detection from user text input
- 🎵 Music recommendations based on detected mood
- 🔍 Rule-based NLP using keyword matching
- 📺 YouTube API integration for real-time video suggestions
- 🌐 Simple and interactive web interface

---

## 🧠 How It Works

1. User enters their current mood as text
2. The system processes the text input
3. Keywords are matched against predefined emotion categories
4. Emotion is detected (Happy, Sad, Angry, Romantic, Calm, Energetic, Neutral)
5. Relevant music videos are fetched using YouTube API
6. Results are displayed to the user

---

## 🤖 Emotion Detection Logic

This project uses a **rule-based NLP approach** instead of a machine learning model.

- Predefined keyword sets for each emotion
- Counts matching words in user input
- Selects emotion with highest score
- Handles edge cases like "not happy" → Sad
- Defaults to "Neutral" if no keywords match

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Logic:** Rule-based NLP (Keyword Matching)
- **API:** YouTube Data API

---

## 📂 Project Structure

```
emotion-music-reccomender/
│── static/              # CSS, JS files
│── templates/           # HTML files
│── youtube_api.py       # YouTube API integration
│── app.py               # Main Flask app
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/tecmeckc/emotion-music-reccomender.git
cd emotion-music-reccomender
```

### 2. Install dependencies

```bash
pip install flask requests
```

### 3. Set up YouTube API Key

- Create a project on Google Cloud Console
- Enable YouTube Data API v3
- Generate an API key
- Add it inside `youtube_api.py`

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Example

| Input Text              | Detected Mood | Recommendation Type     |
|------------------------|--------------|--------------------------|
| "I feel amazing today" | Happy        | Pop / Energetic Songs    |
| "I am feeling low"     | Sad          | Calm / Soft Music        |
| "I'm so angry"         | Angry        | Intense / Rock Music     |

---

## 💡 Use Cases

- 🎧 Personalized music experience
- 🧠 Mood-based recommendations
- 💬 Chat-based entertainment systems
- ❤️ Basic emotional support through music

---

## 📸 Screenshots

### 🏠 Home Page
<p align="center">
  <img src="https://github.com/user-attachments/assets/4cbb4f67-8eae-4206-a4e2-dc531cb5bcc5" width="700"/>
</p>

### 🎵 Recommendation Results
<p align="center">
  <img src="https://github.com/user-attachments/assets/09314a28-b2a5-4216-b207-55a6cd8012c5" width="700"/>
</p>

---

## 🌐 Live Demo

Currently not deployed

---

## 📌 Future Enhancements

- 🤖 Machine Learning-based emotion detection
- 🎥 Facial emotion recognition
- 🎧 Spotify API integration
- 📱 Mobile-friendly UI

---

## 👩‍💻 Author

**Khyati Choudhary**  
- GitHub: https://github.com/tecmeckc  

---

## ⭐ Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.
