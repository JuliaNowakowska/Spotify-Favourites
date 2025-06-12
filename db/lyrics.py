from dataclasses import dataclass

@dataclass
class Lyrics:
    genius_id: str
    spotify_id: str
    lyrics: str