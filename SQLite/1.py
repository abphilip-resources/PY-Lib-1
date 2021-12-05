import sqlite3                                # SQLite3 is a built-in module
file = "allen.db"                             # Database name to be created
  
try:
  conn = sqlite3.connect(file)                # Connect to the database 
  print("Database allen.db formed")        
  cursor = conn.cursor()                      # Create a cursor object
  print('DB initialized')

  query = 'SELECT SQLITE_VERSION();'          # SQLite version Query 
  cursor.execute(query)                       # Execute the Query
  result = cursor.fetchall()                  # Fetch all the rows from the Query output
  print('SQLite Version is {}'.format(result))

except: print("Database allen.db not formed")
  
finally:                      
    if(conn):
        cursor.close()                        # Close the cursor
        conn.commit()                         # commit the transaction
        conn.close()                          # Close the connection
        print("Database allen.db connection closed")