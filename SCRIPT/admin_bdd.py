import mariadb
import sys

def connect_2_bdd():
    '''
    @output : 
        cursor : return le cursor pour gérer les requetes sur la BDD
        connection : return la variable de connection
    '''
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
        
    return (cursor, connection)


def disconnect_2_bdd(connection):
    connection.close()
    

def get_id_ronde():
    '''
    @output 
        int : numéro de la dernière ronde ajouté
    '''
    (cursor, connection) = connect_2_bdd()
    
    cursor.execute("SELECT MAX(ID_RDE) FROM RONDE;",)
    
    for value in cursor:
        id_rde = value
    
    disconnect_2_bdd(connection)
    
    return(id_rde[0])


