#!/usr/bin/env python

import spotipy
import spotipy.util as util
import configparser
import hiphopheads


def init():
    config = configparser.ConfigParser()
    config.read('test.ini')
    scope = 'playlist-modify-public'
    token = spotipy.util.prompt_for_user_token("patrickferry42",
                                               scope=scope,
                                               client_id=config['test']['client_id'],
                                               client_secret=config['test']['client_secret'],
                                               redirect_uri=config['test']['redirect_uri'])
    return spotipy.Spotify(auth=token), config['test']['playlist_uri']


# def close_match(songs, query):

hot = hiphopheads.get_hot(1000)
print(hot)

client, playlist = init()
for name in hot:
    name = name.replace('[FRESH]', '')
    try:
        artist, song = name.split('-')
        print(song)
        songs = [(x['name'], x['artists'][0]['name'], x['id']) for x in client.search(q=song, type='track')['tracks']['items']]
        # print(songs)

        # if len(songs) < 1:
        #
        #     continue
        song = songs[0]

        # print(client.user_playlist('patrickferry42', playlist_id=playlist))
        items = [x['track']['id'] for x in client.user_playlist_tracks('patrickferry42', playlist_id=playlist)['items']]
        if song[2] not in items:
            client.user_playlist_add_tracks('patrickferry42', playlist_id=playlist, tracks=[songs[0][2]])
    except Exception as e:
        with open('nofind.txt', 'a+') as f:
            f.write(name + "  ,  " + str(e) + "\n")
    # print(items)

