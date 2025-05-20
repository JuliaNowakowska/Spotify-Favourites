from spotify_client import SpotifyClient
from db import Database
from spotify_dashboard import Dashboard

def main():
    db = Database()
    client = SpotifyClient()
    dashboard = Dashboard()

    tracks = client.get_top_tracks()
    for track in tracks['items']:
        temp_track = client.extract_track_data(track)
        db.insert_track(temp_track)

    top_track = db.get_top_track()

    dashboard.show(top_track[0][1])

if __name__ == "__main__":
    main()
