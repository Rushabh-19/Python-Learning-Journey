import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksdb.sqlite')
curr = conn.cursor()

# Making fresh tables using executescript()
curr.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;

        CREATE TABLE ARTIST (
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
           name TEXT UNIQUE
        );

        CREATE TABLE Album (
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
           artist_id NUMBER,
           title TEXT UNIQUE
        );

        CREATE TABLE Track (
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
           title NUMBER UNIQUE,
           album_id NUMBER,
           len NUMBER,
           rating NUMBER,
           count INTEGER
        );
''')

fname = input('Enter the file name:')
if len(fname) < 1 : fname = 'tracks/Library.xml'
    
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

#this above data is what we want to retieve from the XML file.

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print ('Dict found:', len(all))

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue)
    
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None:
        continue
    
    print (f'name : {name}, artist: {artist}, album: {album}, count: {count}, rating: {rating}, length: {length}')
    
    curr.execute ('''INSERT OR IGNORE INTO Artist (name)
                    VALUES (?)''', (artist,))
    curr.execute ('''SELECT id FROM Artist WHERE name = ?''', (artist,))
    artist_id = curr.fetchone()[0]
    
    curr.execute ('''INSERT OR IGNORE INTO Album (title, artist_id)
                    VALUES (?,?)''', (album, artist_id))
    curr.execute ('''SELECT id FROM Album WHERE title = ?''', (album,))
    album_id = curr.fetchone()[0]
           
    curr.execute('''INSERT OR REPLACE INTO TRACK 
                   (title, album_id, len, rating, count)
                   VALUES (?, ?, ?, ?, ?)''', (name, artist_id, length, rating, count))
    conn.commit()