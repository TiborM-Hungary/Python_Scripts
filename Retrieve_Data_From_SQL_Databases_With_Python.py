# SQL has many versions, using them is similar
# Using SQLite here

import sqlite3

# Establish connection with the DB, use DB path
con = sqlite3.connect('database.db')

# Cursor object - object that looks at the rows and gives you data
cur = con.cursor()

# Execute the SQL query, execute returns the result set, accessible via cur's methods
# NOTE: use double-quotes, as the query can have single-quotes
# NOTE: once a method is called on cur after executed, it becomes an empty list;
# only can use it once, then have to execute the query again to get the data back in it
# -----------------------------------------------
# Get all data
cur.execute("SELECT * FROM 'table_01' ORDER BY column_01")
# Print output the result set
print(cur.fetchall())

# -----------------------------------------------
# Get specific column
cur.execute("SELECT address, column_01 FROM 'table_01' ORDER BY column_01")
# Print output the result set
print(cur.fetchall())

# -----------------------------------------------
# Get rows where column_01 is less than 300
cur.execute("SELECT * FROM 'table_01' WHERE column_01 < 300")
# Print output the result set
print(cur.fetchall())

# -----------------------------------------------
# Get rows where column_01 is 144
cur.execute("SELECT * FROM 'table_01' WHERE column_01 = 144")
# Print output the result set
print(cur.fetchall())

# -----------------------------------------------
# Get rows where column_01 is less than 300 AND ends with sa
cur.execute(
    "SELECT * FROM 'table_01' WHERE column_01 < 300 AND column_02 LIKE '%sa'")
# Print output the result set
print(cur.fetchall())
