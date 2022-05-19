import mariadb
import sys

try:
    # connection parameters
    conn_params = {
        'user' : "u716502433_PTC",
        'password' : "6B:cY+]s",
        'host' : "185.224.137.3",
        'port' : 3306,
        'database' : "u716502433_PTC"
    }

    # establish a connection
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print("bonsoir")
print(cursor)

print(cursor.execute("SELECT * FROM UTILISATEUR"))

for i in cursor:
    print(i)
    
cursor.execute("INSERT INTO UTILISATEUR (LOGIN_USR,PASSWD_USR) VALUES ('BATON Golden', 'Ogun')")

print(cursor.execute("SELECT * FROM UTILISATEUR"))

for i in cursor:
    print(i)
    
connection.commit()