from transformers import AutoTokenizer, AutoModelForSequenceClassification

class EmotionClassifier:
    def __init__(self, db, model_name="j-hartmann/emotion-english-distilroberta-base"):
        self.db = db
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = self.model.config.id2label