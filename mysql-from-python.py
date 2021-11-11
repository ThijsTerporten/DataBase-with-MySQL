import os
import pymysql

# Get username from cloud9 workspace
# Modify this if running on another environment

username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(
    host='localhost',
    user=username,
    password='',
    db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()