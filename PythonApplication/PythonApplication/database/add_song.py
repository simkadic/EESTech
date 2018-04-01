def func(album, song, minutes, seconds, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    s = "INSERT INTO song (album_id,song_minutes,song_seconds,song_title) "
    s += "SELECT album_id, "
    s += "%s, " % (minutes)
    s += "%s, " % (seconds)
    s += "'%s\' " % (song)
    s += "FROM album WHERE "
    s += "album_name='%s' ;" % (album)
    print(s)
    cursor.execute(s)
    # Cleanup
    conn.commit()
    cursor.close()
    return "OK"
