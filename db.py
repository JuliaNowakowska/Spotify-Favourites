import sqlite3
from config import DB_FILE
from track import Track

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS top_tracks (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    artists TEXT NOT NULL,
                    popularity INTEGER,
                    duration_ms INTEGER,
                    url TEXT
                )
            ''')

    def insert_track(self, track: Track):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO top_tracks (id, name, artists, popularity, duration_ms, url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (track.id, track.name, track.artists, track.popularity, track.duration_ms, track.url))

    def get_all_tracks(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM top_tracks')
        rows = cursor.fetchall()
        return [Track(*row) for row in rows]

    def get_top_track(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM top_tracks LIMIT 1')
        top_track = cursor.fetchall()
        return top_track

