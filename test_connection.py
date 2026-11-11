
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Poojitha@123",
    database="elicit_blogs"
)

if connection.is_connected():
    print("Successfully connected to MySQL!")

connection.close()
