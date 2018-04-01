def func(arg, conn):
    cursor = conn.cursor()
    cursor.execute("use eestec;")
    q = "Select * from country where country_name='%s';"
    cursor.execute(q, arg)
    cursor.fetchall()
    rows_count = cursor.rowcount
    if (rows_count==0): 
        s = "INSERT INTO country (country_name) VALUES('%s');"
        print(s, arg)
        cursor.execute(s)
        # Cleanup
        conn.commit()
    cursor.close()
    return "OK"
