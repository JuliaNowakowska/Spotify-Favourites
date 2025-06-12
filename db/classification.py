from dataclasses import dataclass

@dataclass()
class Classification:
    genius_id: str
    predicted_label: str
    confidence: float