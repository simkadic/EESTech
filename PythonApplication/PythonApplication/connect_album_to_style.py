def func(album,style):
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
        s = "INSERT INTO album_style (album_id,style_id) "
        s += "SELECT album_id, style_id FROM album,style WHERE "
        s += "album_name='%s\' " % (album)
        s += "and style_name='%s\';" % (style)
        print(s)
        cursor.execute(s)
        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
        return "OK"
