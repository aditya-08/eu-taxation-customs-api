import sqlite3, csv

con = sqlite3.connect("italy.db") ## these statements belong outside the loop
cursor = con.cursor()  ## execute them just once

first = True
with open ('checkDigitIT.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    columns = [h.strip() for h in columns]
    if first:
        # cursor.execute('DROP TABLE CheckDigitIT')
        sql = 'CREATE TABLE CheckDigitIT (%s)' % ', '.join(['%s text'%column for column in columns])
        # print (sql)
        cursor.execute(sql)
        first = False
    #~ for row in reader:    ## we will read the rows later in the loop
        #~ print(row)

    query = 'insert into CheckDigitIT({0}) values ({1})'
    # print(query)
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    # print(query)
    cursor = con.cursor()
    for row in reader:
        # print(row)
        cursor.execute(query, row)
    con.commit()

    sql_test = 'select valueEven from CheckDigitIT where app = \'A\''
    result = cursor.execute(sql_test)
    print(result.fetchone()[0])
    con.close()
