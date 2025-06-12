from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

class EmotionClassifier:
    def __init__(self, model_name="j-hartmann/emotion-english-distilroberta-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = self.model.config.id2label

    def classify_emotions(self, lyrics_database):
        lyrics_db = lyrics_database.get_lyrics()

        predictions = []

        for id, lyrics in lyrics_db:
            # Tokenize and prepare input
            inputs = self.tokenizer(lyrics, return_tensors="pt", truncation=True)

            # Run through model
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits

            # Convert logits to probabilities
            probs = F.softmax(logits, dim=-1)

            # Get predicted label
            predicted_class_id = torch.argmax(probs, dim=-1).item()
            predicted_label = self.model.config.id2label[predicted_class_id]
            confidence = probs[0][predicted_class_id].item()

            predictions.append([id, predicted_label, confidence])

        return predictions