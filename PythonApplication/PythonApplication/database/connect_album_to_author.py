def func(album,author, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    s = "INSERT INTO album_author (album_id,author_id) "
    s += "SELECT album_id, author_id FROM author,album WHERE "
    s += "author_name='%s\' " % (album)
    s += "and album_name='%s\';" % (author)
    print(s)
    cursor.execute(s)
    # Cleanup
    conn.commit()
    cursor.close()
    return "OK"
