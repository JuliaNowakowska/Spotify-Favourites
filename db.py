import sqlite3
from config import DB_FILE
from track import Track
from lyrics import Lyrics
from classification import Classification

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self._create_table()

    def _create_table(self):
        with self.conn:
            # Spotify table
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS spotify_tracks (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    artists TEXT NOT NULL,
                    url TEXT
                )
            ''')

            # Genius table
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS lyrics(
                    genius_id TEXT PRIMARY KEY,
                    spotify_id TEXT NOT NULL,
                    lyrics TEXT NOT NULL,
                    FOREIGN KEY (spotify_id) REFERENCES favourite_tracks(id)
                )
            ''')

            # Emotion classification table
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS emotions(
                    genius_id TEXT PRIMARY KEY,
                    predicted_label TEXT NOT NULL,
                    confidence FLOAT
                )
            ''')


    def insert_track(self, track: Track):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO spotify_tracks (id, name, artists, url)
                VALUES (?, ?, ?, ?)
            ''', (track.id, track.name, track.artists, track.url))

    def insert_lyrics(self, lyrics: Lyrics):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO lyrics (genius_id, spotify_id, lyrics)
                VALUES (?, ?, ?)
            ''', (lyrics.genius_id, lyrics.spotify_id, lyrics.lyrics))

    def insert_classification(self, classification: Classification):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO emotions (genius_id, predicted_label, confidence)
                VALUES (?, ?, ?)
            ''', (classification.genius_id, classification.predicted_label, classification.confidence))

    def get_all_tracks(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM spotify_tracks')
        rows = cursor.fetchall()
        return [Track(*row) for row in rows]

    def get_lyrics(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT genius_id, lyrics FROM lyrics')
        rows = cursor.fetchall()
        return [[genius_id, str(lyrics)] for genius_id, lyrics in rows]

    def get_top_track(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM spotify_tracks LIMIT 1')
        top_track = cursor.fetchall()
        return top_track

    def get_track_artist(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, artists FROM spotify_tracks')
        rows = cursor.fetchall()
        return [(row) for row in rows]
