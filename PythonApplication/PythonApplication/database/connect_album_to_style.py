def func(album,style, conn):
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
    return "OK"
