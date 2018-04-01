def func(album, country, day, month, year, format, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    release_date = '%02d' % day + "-" + '%02d' % month + "-" + str(year)

    s = "INSERT INTO version_format (version_id,format_id) "
    s += "SELECT version_id, format_id FROM version,format WHERE "
    s += "format_name='%s\' " % (format)
    s += "and release_date=STR_TO_DATE"
    s += "('%s\', '%%d-%%m-%%Y') " % (release_date)
    s += "and album_id= (select album_id from album "
    s += "where album_name='%s\') " % album
    s += "and country_id= (select country_id from country "
    s += "where country_name='%s\');" % country
    print(s)
    cursor.execute(s)
    # Cleanup
    conn.commit()
    cursor.close()
    return "OK"
