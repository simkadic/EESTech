def func(album,genre, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    s = "INSERT INTO album_genre (album_id,genre_id) "
    s += "SELECT album_id, genre_id FROM album,genre WHERE "
    s += "album_name='%s\' " % (album)
    s += "and genre_name='%s\';" % (genre)
    print(s)
    cursor.execute(s)
    # Cleanup
    conn.commit()
    cursor.close()
    return "OK"
