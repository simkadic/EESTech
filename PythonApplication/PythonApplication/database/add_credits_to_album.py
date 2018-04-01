def func(album, author, role, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    s = "INSERT INTO credits (album_id,author_id, role_id) "
    s += "SELECT album_id, author_id, role_id " 
    s += "FROM author,album,role WHERE "
    s += "author_name='%s\' " % (album)
    s += "and role_name='%s\' " % (role)
    s += "and album_name='%s\';" % (author)
    print(s)
    cursor.execute(s)
    # Cleanup
    conn.commit()
    cursor.close()
    return "OK"
