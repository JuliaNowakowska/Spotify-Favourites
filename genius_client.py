from lyricsgenius import Genius
from config_genius import TOKEN

class GeniusClient:
    def __init__(self):
        self.client = Genius(TOKEN)

    def get_song_id(self, track, artist):
        """
        This method finds a song in the Genius database and returns its ID or the ID of the parent,
        in case the song found is a translation of other song.
        :param track: name of the track
        :param artist: name of the artist
        :return: track ID
        """
        # first finding song in genius to be able to extract its ID
        song_found = self.client.search_song(track, artist)
        if not song_found:
            return None

        # finding song data based on the ID
        song_data = self.client.song(song_found.id)
        # identifying all related songs
        related_songs = song_data.get("song", {}).get("song_relationships", [])
        # loop through the related songs to find if it is a translation of any other song
        for related in related_songs:
            # if so -> return the parent's ID
            if related["relationship_type"] == "translation_of" and related.get("songs"):
                return related["songs"][0]["id"]
        # otherwise return the song id, as this is the OG song
        return song_found.id



