def func(arg, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    q = "Select * from style where style_name='%s';"
    cursor.execute(q, arg)
    cursor.fetchall()
    rows_count = cursor.rowcount
    if (rows_count==0): 
        s = "INSERT INTO style (style_name) VALUES('%s');"
        print(s)
        cursor.execute(s, arg)
        # Cleanup
        conn.commit()
    cursor.close()
    return "OK"
