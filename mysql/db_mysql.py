import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS syn_college")
cursor.execute("USE syn_college")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 22))

conn.commit()

print("Done!")