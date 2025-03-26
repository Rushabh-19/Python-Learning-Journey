import sqlite3

conn = sqlite3.connect ('assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts (org TEXT,count INTEGER)')


fname = input('Enter the file name: ')
if len(fname) < 1: fname = '../mbox-short.txt'

fh = open (fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    domain = pieces[1].split('@')[1]
    
    cur.execute('SELECT count FROM counts WHERE org = ?', (domain,))
    
    row = cur.fetchone()
    
    if row is None:
        cur.execute('INSERT INTO counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE counts SET count = count + 1 WHERE org = ?', (domain,))
    

conn.commit()

#https://www.sqlite.org/lang_select.html

main_query = '''
                  SELECT org,count 
                  FROM counts 
                  ORDER BY count DESC
                  LIMIT 10
             '''

for row in cur.execute(main_query):
    print(str(row[0]) , row[1])

cur.close()