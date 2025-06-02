from spotify_client import SpotifyClient
from genius_client import GeniusClient
from db import Database
from lyrics import Lyrics

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
    for spotify_id, track, artist in artist_track:
        genius_id = genius.get_song_id(track, artist)

        # If the song is found on Genius, insert it to our database
        if genius_id:
            lyrics_text = genius.client.lyrics(song_id=genius_id, remove_section_headers=True)
            lyrics = Lyrics(genius_id, spotify_id, lyrics_text)
            db.insert_lyrics(lyrics)


if __name__ == "__main__":
    main()
