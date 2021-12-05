import sqlite3
file = "allen.db"
  
try:
  conn = sqlite3.connect(file)
  cursor = conn.cursor()

  # Create table, drop if already existing
  cursor.execute('DROP TABLE IF EXISTS STUDENT')
  table = """CREATE TABLE STUDENT(
              NAME VARCHAR(255), 
              CLASS VARCHAR(255),
              MARKS INT,
              SECTION VARCHAR(255));""" 
  cursor.execute(table)

  # Insert Values to the table
  cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 91, 'A')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 45, 'B')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 22, 'C')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Ramesh', '10th', 70, 'D')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Suresh', '11th', 82, 'E')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Sai', '12th', 94, 'F')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Sri', '6th', 68, 'G')''')
  cursor.execute('''INSERT INTO STUDENT VALUES ('Sita', '5th', 53, 'H')''')

  # User input of values into the table
  ans=[]
  for _ in range(int(input())):
    print("\nEntry {}:".format(_+1))
    l=[]
    n,c,m,s=input(),input(),int(input()),input()
    l.extend([n,c,m,s])
    l=tuple(l)
    ans.append(l)
  cursor.executemany('''INSERT INTO STUDENT VALUES (?, ?, ?, ?)''',ans)

  # SELECT Command with for loop
  data = cursor.execute('''SELECT * FROM STUDENT''')
  print("\nName | Class | Marks | Section")
  for z in data: print(z[0]," | ",z[1]," | ",z[2]," | ",z[3])

except: print("Not Working")
  
finally:
    if(conn):
        cursor.close()              # close the cursor
        conn.commit()               # commit the transaction
        conn.close()                # close the connection