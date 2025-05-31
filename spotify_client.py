import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from track import Track

class SpotifyClient:
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="user-top-read"
        ))

    def get_tracks(self):
        return self.client.current_user_top_tracks(time_range="long_term")

    def extract_track_data(self, track):
        return Track(
            id=track["id"],
            name=track["name"],
            artists=', '.join([artist['name'] for artist in track['artists']]),
            url=track["href"]
        )
