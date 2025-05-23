from reddit_fetcher import get_reddit_trends
import json
import os

FAV_FILE = "favorites.json"

def get_fomo_data():
    # This calls Reddit trends
    return get_reddit_trends()

def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r") as f:
            return json.load(f)
    return []

def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f, indent=4)

