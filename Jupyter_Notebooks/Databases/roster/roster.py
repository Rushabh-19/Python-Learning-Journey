import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
curr = conn.cursor()

#lets setup a executescrupt()

curr.executescript('''
      DROP TABLE IF EXISTS User;
      DROP TABLE IF EXISTS Course;
      DROP TABLE IF EXISTS Member;
      
      CREATE TABLE User(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          name TEXT UNIQUE
      );
      
      CREATE TABLE Course(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
          title TEXT UNIQUE
      );
      
      CREATE TABLE Member(
          user_id INTEGER,
          course_id INTEGER,
          role INTEGER,
          PRIMARY KEY (user_id, course_id)
      );
''')

fname = input ('Enter the file name:')
if len(fname) < 1: fname = 'roster_data.json'
    
# [
#    ["Charley", "sill0", 1],
#    ["Mea", "sill0", 0], 

str_data = open (fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    
    print(f'name: {name}, title: {title}, role: {role}')
    
    curr.execute('''INSERT OR IGNORE INTO User (name)
          VALUES(?)''', (name, ))
    curr.execute('''SELECT id FROM User WHERE name = ?''', (name, ))
    user_id = curr.fetchone()[0]
    
    curr.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES(?)''', (title, ))
    curr.execute('''SELECT id FROM Course WHERE title = ?''', (title, ))
    course_id = curr.fetchone()[0]
    
    curr.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
    VALUES(?, ?, ?)''', (user_id, course_id, role))
    
    conn.commit()