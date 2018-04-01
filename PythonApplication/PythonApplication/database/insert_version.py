def func(album, country, day, month, year, conn):
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
    return "OK"
