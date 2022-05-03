from admin_bdd import connect_2_bdd, disconnect_2_bdd
from formatage_1 import formatage_1

def add_ronde_bdd(data):
    '''
    TO-DO :
        
    
    @input : 
        
    
    @output : 
        
    '''    
    (cursor, connection) = connect_2_bdd()
    requete = "INSERT INTO RONDE (TPS_RDE,DATE_RDE) VALUES " + data
    print(requete)
    
    cursor.execute(requete)

    connection.commit()
    
    #print(connection)
    disconnect_2_bdd(connection)
    #print(connection)

data = "(000, '2022-05-03 16:29:32.555116');"
add_ronde_bdd(data)