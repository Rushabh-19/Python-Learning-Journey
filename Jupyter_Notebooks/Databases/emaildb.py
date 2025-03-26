import sqlite3

conn = sqlite3.connect ('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts_Email')

cur.execute('CREATE TABLE Counts_Email (email TEXT,count INTEGER)')

fname = input('Enter the file name: ')
if len(fname) < 1: fname = '../mbox-short.txt'

fh = open (fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    
    cur.execute('SELECT count FROM Counts_Email WHERE email = ?', (email,))
    
    row = cur.fetchone()
    
    if row is None:
        cur.execute('INSERT INTO Counts_Email (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts_Email SET count = count + 1 WHERE email = ?', (email,))
    
    conn.commit()

#https://www.sqlite.org/lang_select.html

main_query = '''
                  SELECT email,count 
                  FROM Counts_Email 
                  ORDER BY count DESC 
                  LIMIT 10
             '''

for row in cur.execute(main_query):
    print(str(row[0]) , row[1])

cur.close()