from gmusicapi import Mobileclient

def getpass():
    return 'Gmusicpass!'


api = Mobileclient()
api.login('yahia.abaza@mendeley.com', getpass())



def add_tracks_to_library(query):
    i=0
    results = api.search_all_access(query,max_results=100)
    albums = results['album_hits']
    songs = results['song_hits']
    for song in songs:
        api.add_aa_track(song['track']['nid'])



def add_all_tracks_to_playlists(playlist_name):
    '''Takes str of playlist name and returns 1000 songs in a number of playlists '''
    library = api.get_all_songs()
    all_track_ids = [track['id'] for track in library]
    #create buckets
    buckets=[]
    for i in range(len(all_track_ids)//1000+1):
        buckets+=[[]]
    i = 0
    for playlist in buckets:
        #fill buckets up to 1000 tracks
        p=0
        while p < 1000 and i<len(all_track_ids):
            playlist+=[all_track_ids[i]]
            i+=1
            p+=1
    pn = 1
    for b in buckets:
        #create playlist for each bucket
        playlist_id = api.create_playlist(playlist_name+str(pn))
        pn+=1
        api.add_songs_to_playlist(playlist_id, b)



def get_the_space_party_started(words):
    for word in words:
        print word
        add_tracks_to_library(word)
    add_all_tracks_to_playlists('Time for a Space Party!')


space_words = ['space','rocket']

get_the_space_party_started(space_words)

print 'ROCK ON!!!'


space_words2=['space','rocket','laser',
             'eclipse','corona','nebula',
             'spaceship','star','galaxy',
             'alien','martian','andromeda']