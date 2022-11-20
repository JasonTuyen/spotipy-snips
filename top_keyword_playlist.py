from ast import keyword
from tkinter import N
from unicodedata import name
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Sign Up for Spotify Developer API and then copy and paste your id and secret keys
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="ID",
                                                           client_secret="SECRET"))

#Insert keyword search term below
keywords='KEYWORD'

#Calls Spotify API using Spotipy Library to find songs in the top playlists relating to keyword above
id_list = []
list_of_tracks = []
list_of_ids = []

results = sp.search(q=keywords, limit=10, offset=0, type='playlist')
for idx, items in enumerate(results['playlists']['items']):
    id_list.append(items['id'])

for idx, ids in enumerate(id_list):
    result = sp.playlist_items(playlist_id = ids, fields='items(track(name, id))', limit=5, offset=0)
    for idx, songs in enumerate(result['items']):
        list_of_tracks.append(songs['track']['name'])
        list_of_ids.append(songs['track']['id'])

#Outputs results to external text file
f = open('output.txt', 'w')
for i in range(0, len(list_of_ids)):
    url = "https://open.spotify.com/track/" + list_of_ids[i]
    print(url, '%s' %list_of_tracks[i], file=open('output.txt', 'a'))
