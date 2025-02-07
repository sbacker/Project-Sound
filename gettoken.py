import spotipy
import spotipy.util as util
import os
import json

# Set Spotify API credentials as environment variables


client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

scope = 'user-library-read'
username = 'DAL' 

token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    
    # Get the first batch of saved tracks
    results = sp.current_user_saved_tracks(limit=50)
    saved_tracks = results['items']
    
    # Continue retrieving tracks until all tracks are fetched
    while results['next']:
        results = sp.next(results)
        saved_tracks.extend(results['items'])

    # Extract track information
    tracks_info = []
    for item in saved_tracks:
        track_info = {
            "id": item['track']['id'],
            "name": item['track']['name'],
            "artist": item['track']['artists'][0]['name']
        }
        tracks_info.append(track_info)

    # Dump to JSON
    with open('data.json', 'w') as fp:
        json.dump(tracks_info, fp)
else:
    print("Can't get token for", username)