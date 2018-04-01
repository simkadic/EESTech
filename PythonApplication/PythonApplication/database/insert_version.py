def func(album, country, day, month, year):
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
        release_date = '%02d' % day + "-" + '%02d' % month + "-" + str(year)
        s = "INSERT INTO version (album_id,country_id,release_date) "
        s += "SELECT album_id, country_id, "
        s += "STR_TO_DATE('%s\', '%%d-%%m-%%Y') " % (release_date)
        s += "FROM album,country WHERE "
        s += "album_name='%s\' " % (album)
        s += "and country_name='%s\';" % (country)
        print(s)
        cursor.execute(s)
        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
        return "OK"
