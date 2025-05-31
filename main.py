from spotify_client import SpotifyClient
from genius_client import GeniusClient
from db import Database

def main():
    db = Database()
    client = SpotifyClient()
    genius = GeniusClient()

    # getting all my favourite tracks from Spotify and saving them to my database
    tracks = client.get_tracks()
    for track in tracks['items']:
        temp_track = client.extract_track_data(track)
        db.insert_track(temp_track)

    # identifying the songs' Genius ID and getting the lyrics
    artist_track = db.get_track_artist()
    for track, artist in artist_track:
        song_id = genius.get_song_id(track, artist)
        if song_id:
            print(genius.client.lyrics(song_id=song_id, remove_section_headers=True))



if __name__ == "__main__":
    main()
