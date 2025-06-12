# Spotify Favourites

This is a Python-based application that integrates with the **Spotify Web API** and **Genius API** to retrieve a user's top tracks, fetch corresponding lyrics, and store this information in a local database. Once the lyrics are stored, I run a **emotions classification model** in order to investigate which emotions dominate in the user's favourite tracks from Spotify.

### Features

- **Spotify Integration:** Authenticates users via OAuth and retrieves their top tracks using the Spotify Web API.
- **Lyrics Retrieval:** Fetches song lyrics from the Genius API for the user's top tracks.
- **Data Storage:** Stores track information and lyrics in a local SQLite database for offline access and analysis.
- **Emotion classification:** Identifies a leading emotion behind every song.
- **Visualization:** Visualize the emotion distribution as a histogram.


### Output
![Screenshot 2025-06-12 at 21 59 23](https://github.com/user-attachments/assets/7326e40c-e2ba-415c-a83d-ba64f940f9f8)
