import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_videos_by_mood(mood):

    mood_queries = {
        "happy": ["happy songs", "feel good songs", "upbeat music"],
        "sad": ["sad songs", "emotional songs", "heartbreak songs"],
        "angry": ["angry songs", "rock music", "intense music"],
        "romantic": ["romantic songs", "love songs", "bollywood love songs"],
        "calm": ["lofi music", "relaxing music", "study music"],
        "energetic": ["party songs", "workout music", "dance songs"],
        "neutral": ["trending songs", "popular music"]
    }

    queries = mood_queries.get(mood, ["songs", "music"])

    videos = []
    seen = set()

    for query in queries:
        url = "https://www.googleapis.com/youtube/v3/search"

        params = {
            "part": "snippet",
            "q": query,
            "key": API_KEY,
            "maxResults": 5,
            "type": "video"
        }

        response = requests.get(url, params=params)
        data = response.json()

        for item in data.get("items", []):
            video_id = item["id"].get("videoId")

            if not video_id or video_id in seen:
                continue

            seen.add(video_id)

            video = {
                "title": item["snippet"]["title"],
                "channel": item["snippet"]["channelTitle"],
                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                "url": f"https://www.youtube.com/watch?v={video_id}"
            }

            videos.append(video)

    return videos