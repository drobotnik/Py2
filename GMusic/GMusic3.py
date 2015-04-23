from gmusicapi import Mobileclient

api = Mobileclient()
api.login('username', 'password')



def add_all_tracks_to_playlists(playlist_name):
    '''Takes str of playlist name and returns playlists of 1000 songs enough for your library'''
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
