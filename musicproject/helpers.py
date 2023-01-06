import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict


# set up spotify api
# insert client_id and client_secret below
client_id = ''
client_secret = ''
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def find_song(name):
    """ Get song data from song name """

    song_data = defaultdict()

    # query for songs with the track name
    results = sp.search(q='{}'.format(name), type="track", limit=1)

    # check if query is empty
    if results['tracks']['items'] == []:
        return None

    # add song data to the dictionary
    results = results['tracks']['items'][0]
    song_data['name'] = [results['name']]
    song_data['artists'] = [results['artists']]
    song_data['img_url'] = [find_image_from_song(song_data['name'], song_data['artists'][0][0]['name'])]

    # return dictionary with song data
    return song_data    


def find_song_with_artist(name, artist):
    """ Get song data from artist and song name """
    
    song_data = defaultdict()

    # query for tracks based on song name and artist
    results = sp.search(q= 'track: {} artist: {}'.format(name, artist), type="track", limit=10)
    
    # check for empty query
    if results['tracks']['items'] == []:
        return None

    # add song data to the dictionary
    results = results['tracks']['items'][0]
    audio_features = sp.audio_features(results['id'])[0]

    song_data['name'] = [results['name']]
    song_data['artists'] = [results['artists']]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]

    for key, value in audio_features.items():
        song_data[key] = value

    # return dictionary with song data
    return song_data 


def find_image_from_song(name, artist):
    """ Get album image from artist and song name  """

    # query spotify api for songs with name and artist
    results = sp.search(q= 'track: {} artist: {}'.format(name, artist), type="track", limit=10)

    # check query returns empty
    if results['tracks']['items'] == []:
        return None
    
    # check if there are images
    if results['tracks']['items'][0]['album']['images'][0] == None:
        return ""

    # query for image url
    image_url = results['tracks']['items'][0]['album']['images'][0]['url']

    if results['tracks']['items'][0]['album']['images'][0]['url'] == None:
        return None
        
    #return the url of the album image
    return image_url
                                     
