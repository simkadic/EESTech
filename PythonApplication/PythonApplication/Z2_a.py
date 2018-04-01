def func():
    import mysql.connector
    from mysql.connector import errorcode

    config = {
        'host': 'eestec.mysql.database.azure.com',
        'user': 'mysql@eestec',
        'password': 'Tesa2018',
        'database': 'mysql'
    }

    # Construct connection string
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()
        cursor.execute("use eestec;")
        s = "SELECT count(*), g.genre_name "
        s += "from album_genre ag, genre g "
        s += "where ag.genre_id=g.genre_id "
        s += "group by g.genre_name;"
        print(s)
        cursor.execute(s)
        rows = cursor.fetchall()
        
        f = open('Z2_a.txt', 'w')
        for row in rows:
            f.write(row[0]+" "+row[1]+"\n")
        f.close();
        # Cleanup
        # conn.commit()
        cursor.close()
        conn.close()
        return "OK"
