import mysql.connector

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="present"
)

mycursor = mydb.cursor()
print("Creating movies database")
mycursor.execute("CREATE DATABASE movies")

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="present",
  database="movies"
)

mycursor = mydb.cursor()
print("Creating titles table")
mycursor.execute("CREATE TABLE titles(name varchar(255) PRIMARY KEY, director varchar(255), year YEAR, country varchar(255), rating varchar(255));")
print("\nCreating hello world movie entry")
mycursor.execute("INSERT INTO movies.titles (name, director, year, country, rating) VALUES ('hello world', 'Tomohiko Ito', 2019, 'Japan', 'average');")
print("\nSelecting world movie entry")
mycursor.execute("SELECT * FROM movies.titles WHERE name = 'hello world';")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print("\nUpdating rating on hello world")
mycursor.execute("UPDATE movies.titles SET rating = 'good' WHERE name = 'hello world';")
print("\nSelecting updated hello world record")
mycursor.execute("SELECT * FROM movies.titles WHERE name = 'hello world';")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print("\nDeleting hello world record")
mycursor.execute("DELETE FROM movies.titles WHERE name = 'hello world';")
mycursor.execute("SELECT * FROM movies.titles WHERE name = 'hello world';")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


