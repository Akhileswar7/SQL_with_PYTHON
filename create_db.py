import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="Akhil@63057")
cr_db="create database Inventoty_Management;"
cur=mydb.cursor()
cur.execute(cr_db)
