import argparse
from spotify_client import SpotifyClient
from genius_client import GeniusClient
from db import Database
from lyrics import Lyrics
from classification import Classification
from emotion_classification import EmotionClassifier

def fetch_spotify_tracks(db, spotify_client):
    tracks = spotify_client.get_tracks()
    for track in tracks['items']:
        temp_track = spotify_client.extract_track_data(track)
        db.insert_track(temp_track)

def fetch_lyrics(db, genius_client):
    artist_track = db.get_track_artist()
    for spotify_id, track, artist in artist_track:
        genius_id = genius_client.get_song_id(track, artist)

        # If the song is found on Genius, insert its lyrics to the database
        if genius_id:
            lyrics_text = genius_client.client.lyrics(song_id=genius_id, remove_section_headers=True)
            lyrics = Lyrics(genius_id, spotify_id, lyrics_text)
            db.insert_lyrics(lyrics)

def classify_songs(db, emotion_classifier):
    classifications = emotion_classifier.classify_emotions(db)

    for id, predicted_label, confidence in classifications:
        new_classification = Classification(id, predicted_label, confidence)
        db.insert_classification(new_classification)

def main():
    parser = argparse.ArgumentParser(description="Fetch Spotify tracks adn Genius lyrics.")
    parser.add_argument('--fetch-spotify', action='store_true', help="Fetch and store your favourite tracks from Spotofy.")
    parser.add_argument('--fetch-lyrics', action='store_true', help="Fetch and store lyrics of your Spotify favourite tracks from Genius.")
    parser.add_argument('--classify-emotions', action='store_true', help="x")

    args = parser.parse_args()

    db = Database()
    spotify_client = SpotifyClient()
    genius_client = GeniusClient()
    emotion_classifier = EmotionClassifier()

    if args.fetch_spotify:
        print("Fetching tracks from Spotify...")
        fetch_spotify_tracks(db, spotify_client)

    if args.fetch_lyrics:
        print("Fetching lyrics from Genius...")
        fetch_lyrics(db, genius_client)

    if args.classify_emotions:
        print("Classifying emotions in songs")
        classify_songs(db, emotion_classifier)

    if not args.fetch_spotify and not args.fetch_lyrics and not args.classify_emotions:
        print("No action specified. Use --fetch-spotify, -fetch-lyrics or --classify-emotions.")


if __name__ == "__main__":
    main()
