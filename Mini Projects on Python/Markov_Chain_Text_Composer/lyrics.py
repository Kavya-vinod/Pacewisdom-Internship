import lyricsgenius

# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("9kH5zsOi5J3OGN-_Pn9jONaPYifnbaz7CsNlZZ_WFydd5AAsnl1lc-4_9ArjgxPQou2hojYAOhJZhVdI2evGdA")

def save_lyrics(songs, artist_name, album_name):
    for i in range(len(songs
    )):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        lyrics = song.lyrics
        with open('songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
            f.writelines(lyrics.split('\\n'))


if __name__ == '__main__':
    songs = [
        'the box',
        'down below',
        'project dreams',
        'die young',
        'boom boom room',
        'high fashion',
        'roll dice',
        'war baby',
        'every season'
    ]
    save_lyrics(songs, 'roddy ricch', '')
