from gmusicapi import Mobileclient
import csv
import unicodecsv


pw = 'fptmuvsatjohyyws'
u = 'ykabaza@gmail.com'

api = Mobileclient()
api.login(u, pw)

#library = api.get_all_songs()
playlists = api.get_all_user_playlist_contents()

trackid = u'9f439f26-7722-3419-ab66-dc47a38f4a10'
plainid = u'7e047d01-3a3e-37b4-a20d-7d927bd0d189'

p=0
for i in playlists:
    print(p)
    p+=1

for i in playlists[:1]:
    for r in i:
        print(r)

for t in playlists[1]['tracks']:
    print(t)

output = []
#for i in library[:5]:
 #   output += [[i['artist'], i['title'], i['album'], i['nid']]]
#
'''
with open('playlists.csv', 'wb') as csvfile:
    writer = unicodecsv.writer(csvfile, dialect='excel', encoding='utf-8')
    for r in output:
        writer.writerow(r)
'''