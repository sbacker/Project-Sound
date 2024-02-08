import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dotenv
from typing import Dict, List
import csv
import math
import time


def main():
    """
    This function sets up the Spotify API credentials and calls the other functions to get the playlist tracks and track details.
    """
    # load the .env file
    dotenv.load_dotenv('.env')

    # Set up Spotify API credentials
    client_id = dotenv.dotenv_values().get('SPOTIFY_CLIENT_ID')
    client_secret = dotenv.dotenv_values().get('SPOTIFY_CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # get playlist tracks
    # get_playlist_tracks(
    #     'https://open.spotify.com/playlist/1fjmiwCMmiwm8Shk38mzu2?si=a3e0e6d188094923', sp, 16)

    # get track details
    song_list = []
    with open('all_songs_ids.txt', 'r') as f:
        for line in f:
            song_list.append(line.split(','))
    track_details = get_track_details(song_list, sp)
    to_csv('track_details.csv', track_details)


def get_playlist_tracks(playlist_url: str, sp: spotipy.Spotify, offset: int = 0) -> None:
    """
    gets playlist tracks and writes to a file

    Args:
        playlist_url (str): URL to the playlist.
        sp (spotipy.Spotify): Spotify object to use, must be authenticated.
        offset (int, optional): # of songs to get in 100s. Defaults to 0.
    """
    write = []

    for i in range(0, offset):
        all_songs = sp.playlist_tracks(playlist_url, offset=i*100)
        for item in all_songs['items']:
            write.append(
                f"{item['track']['id']},{item['track']['name']},{item['track']['artists'][0]['name']},{item['track']['album']['name']}")
    with open('all_songs_ids.txt', 'w') as f:
        f.write('track_id,track_name,artist_name,album_name\n')
        f.writelines("\n".join(set(write)))


def get_track_details(tracks: List[str], sp: spotipy.Spotify) -> Dict[str, Dict[str, str]]:
    """
    gets track details and returns a dictionary

    Args:
        track_id (str): Track ID to get details for
        sp (spotipy.Spotify): Spotify object to use, must be authenticated.
    Returns:
        Dict[str, Dict[str,str]]: A dictionary with track details, where the key is a string of the form
        '{track name} - {artist name} - {album name}', and the value is a dictionary of audio features.
    """
    track_details = {}
    i = 0
    len_tracks = math.ceil(len(tracks))
    stripped_tracks = tracks[1:]
    track_subsets = []
    for j in range(0, len_tracks-1):
        track_subsets.append(stripped_tracks[j*100:(j+1)*100])
    track_subsets.append(stripped_tracks[len_tracks*100:])
    for track_subset in track_subsets:
        print(i)
        i += 1
        ids = [id[0] for id in track_subset]
        try:
            tracks = sp.audio_features(ids)
        except Exception as e:
            print(e)
            break

        for index, track in enumerate(tracks):
            track_subset[index][3] = track_subset[index][3].replace("\\n", "")
            track['track_id'] = track_subset[index][0]
            track['track_name'] = track_subset[index][1]
            track['artist_name'] = track_subset[index][2]
            track['album_name'] = track_subset[index][3]
            track_details[f'{track_subset[index][1]} - {track_subset[index][2]} - {track_subset[index][3]}'] = tracks
        time.sleep(10)  # wait 10 seconds before continuing
    return track_details


def to_csv(file_name: str, track_details: Dict[str, Dict[str, str]]) -> None:
    """
    Writes a dictionary of track details to a CSV file.

    Args:
        file_name (str): The name of the CSV file to write to.
        track_details (Dict[str, Dict[str, str]]): A dictionary of track details, where the key is a string of the form
            '{track name} - {artist name} - {album name}', and the value is a dictionary of audio features.
    """
    with open(file_name, 'w') as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=track_details.keys(), delimiter=',')
        writer.writeheader()
        writer.writerows(track_details.values())


if __name__ == '__main__':
    main()
