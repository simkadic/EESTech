def func(arg, conn):
        cursor = conn.cursor()
        cursors.execute('use eestec;')
        q = "SELECT * from format WHERE format_name=('%s');"
        cursor.execute(q, arg)
        cursor.fetchall()
        row_count = cursor.row_count
        if(row_count == 0):
            s = "INSERT INTO format (format_name) VALUES('%s')"
            cursors.execute(s, arg)
        cursor.close()
        return "OK"
