import pyodbc


def returnSingleValue(text):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-4Q04DN0\\SQLEXPRESS;'
                          'Database=ATMBASIC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(text)

    mycursor = cursor.fetchall()

    val = mycursor[0][0]
    conn.commit()
    conn.close()
    return val


def addInfo(text):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-4Q04DN0\\SQLEXPRESS;'
                          'Database=ATMBASIC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(text)
    conn.commit()
    conn.close()


def returnLargeValue(text):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-4Q04DN0\\SQLEXPRESS;'
                          'Database=ATMBASIC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(text)

    mycursor = cursor.fetchall()

    conn.commit()
    conn.close()
    return mycursor
