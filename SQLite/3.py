import sqlite3
file = "allen.db"

try:
    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    # SELECT Command with for loop
    print("\nSQL Method:")
    data = cursor.execute('''SELECT DISTINCT * FROM STUDENT LIMIT 3''')     
    print("Name | Class | Marks | Section")
    for z in data: print(z[0]," | ",z[1]," | ",z[2]," | ",z[3])

    # SELECT with fetch() method
    cursor.execute('''SELECT * FROM STUDENT ORDER BY NAME LIMIT 3''')
    print("\nFetch in Python 1:")
    print(cursor.fetchall())
    # Same output will be created in both the cases
    cursor.execute('''SELECT * FROM STUDENT ORDER BY NAME''')
    print("\nFetch in Python 2:")
    print(cursor.fetchmany(3))

    # Updation and Deletion, SELECT to check
    cursor.execute("DELETE FROM STUDENT WHERE MARKS<40")
    cursor.execute("UPDATE STUDENT SET NAME = 'Sam' WHERE SECTION='H'")
    print("\nChanged Data:")
    data = cursor.execute('''SELECT * FROM STUDENT ORDER BY SECTION DESC''')
    print("Name | Class | Marks | Section")
    for z in data: print(z[0]," | ",z[1]," | ",z[2]," | ",z[3])

    # Reversal of previous action, SELECT to check
    cursor.execute("DELETE FROM STUDENT WHERE SECTION='H'")
    cursor.execute('''INSERT INTO STUDENT VALUES ('Sita', '5th', 53, 'H')''')
    cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 22, 'C')''')
    print("\nRetrieved Data:")
    data = cursor.execute('''SELECT * FROM STUDENT ORDER BY SECTION DESC''')
    print("Name | Class | Marks | Section")
    for z in data: print(z[0]," | ",z[1]," | ",z[2]," | ",z[3])

    # Reversal is also possible with cursor.rollback()

except: print("Not Working")

finally:
    if(conn):
        cursor.close()              # close the cursor
        conn.commit()               # commit the transaction
        conn.close()                # close the connection