from dataclasses import dataclass

@dataclass
class Track:
    id: str
    name: str
    artists: str
    popularity: int
    duration_ms: int
    url: str
