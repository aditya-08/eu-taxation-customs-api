import sqlite3, csv

con = sqlite3.connect("italy.db") ## these statements belong outside the loop
cursor = con.cursor()  ## execute them just once

first = True
with open ('CodeList.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    columns = [h.strip() for h in columns]
    if first:
        sql = 'CREATE TABLE IF NOT EXISTS CodeList (%s)' % ', '.join(['%s text'%column for column in columns])
        print (sql)
        cursor.execute(sql)
        first = False
    #~ for row in reader:    ## we will read the rows later in the loop
        #~ print(row)

    query = 'insert into CodeList({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    print(query)
    cursor = con.cursor()
    for row in reader:
        cursor.execute(query, row)
    con.commit()
    con.close()
