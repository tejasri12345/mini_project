import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",database="details")

# Get a cursor
cur = cnx.cursor()

# Execute a query
# cur.execute("SELECT CURDATE()")

# Close connection
cnx.close()