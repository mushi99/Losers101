import mysql.connector
from mysql.connector import errorcode

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="videobrowsing"
  )
  mycursor = mydb.cursor()

  query = ("SELECT * FROM topics")

  mycursor.execute(query)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  mycursor.close()
  mydb.close()


