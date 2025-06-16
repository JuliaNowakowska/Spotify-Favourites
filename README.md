# Spotify Favourites

This is a Python-based application that integrates with the **Spotify Web API** and **Genius API** to retrieve a user's top tracks, fetch corresponding lyrics, and store this information in a local database. Once the lyrics are stored, an **emotion classification model** is used in order to investigate which emotions dominate in the user's favourite tracks from Spotify.

<div align="center">
  <img src="https://github.com/user-attachments/assets/203298ed-03fe-460c-9e5c-1e3a9ff64d75" width="600"/>
</div>


### Data 
The data is stored in a local SQLite database, organized into three tables. The first table, spotify_tracks, contains Spotify IDs, names, artists, and URLs of the user's favourite tracks as fetched using Spotify API. The lyrics table stores the original-language lyrics of the tracks listed in spotify_tracks. However, not all tracks have corresponding lyrics, as some could not be found. The emotions table includes emotion labels and confidence scores for the tracks, generated using the emotion-english-distilroberta-base model by J-Hartmann, categorizing each song based on its emotional content.
![Screenshot 2025-06-16 at 10 47 15](https://github.com/user-attachments/assets/9eb595d0-400b-474f-83c7-cae33d616dd7)


### Model
The model used to categorize songs into emotions was published by J-Hartmann on Hugging Face (https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) and is a finetuned version of DistilRoBERTa-base model. It classify text into 6 emotions: anger, disgust, fear, joy, neutral, sadness and surprise.

### Sample Output
The output of the project is a distribution of emotions in the user's top tracks. Below is a sample output for my favourite songs :)
<div align="center">
  <img src="https://github.com/user-attachments/assets/7326e40c-e2ba-415c-a83d-ba64f940f9f8" width="600"/>
</div>

#### Evaluation
Below is the average confidence for each emotion that my favourite tracks were categorized under. Almost all classes achieved confidence levels oscillating aroung 0.5, which indicates how complex the task is as often a song cannot be summarized under one emotion.

| Emotion  | Average Confidence |
|----------|--------------------|
| Surprise | 0.71               |
| Fear     | 0.56               |
| Sadness  | 0.54               |
| Neutral  | 0.47               |
| Anger    | 0.44               |
| Joy      | 0.47               |
