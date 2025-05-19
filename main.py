from spotify_client import SpotifyClient
from db import Database

def main():
    db = Database()
    client = SpotifyClient()

    tracks = client.get_top_tracks()
    for track in tracks['items']:
        temp_track = client.extract_track_data(track)
        db.insert_track(temp_track)

if __name__ == "__main__":
    main()
