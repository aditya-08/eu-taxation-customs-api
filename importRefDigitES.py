
import sqlite3, csv

con = sqlite3.connect("spain.db") ## these statements belong outside the loop
cursor = con.cursor()  ## execute them just once

first = True
with open ('RefDigitES.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    columns = [h.strip() for h in columns]
    if first:
        # cursor.execute('DROP TABLE RefD#igitES')
        sql = 'CREATE TABLE RefDigitES (%s)' % ', '.join(['%s text'%column for column in columns])
        print (sql)
        cursor.execute(sql)
        first = False
    #~ for row in reader:    ## we will read the rows later in the loop
        #~ print(row)

    query = 'insert into RefDigitES({0}) values ({1})'
    # print(query)
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    # print(query)
    cursor = con.cursor()
    for row in reader:
        # print(row)
        cursor.execute(query, row)
    con.commit()

    sql_test = 'select checkDigit from RefDigitES where dig = \'1\''
    result = cursor.execute(sql_test)
    print(result.fetchone()[0])
    con.close()
