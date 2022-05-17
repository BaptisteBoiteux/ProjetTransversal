from admin_bdd import connect_2_bdd, disconnect_2_bdd

def add_pht_bdd(data):
    '''
    TO-DO :
        Catch les erreurs potentielles
    
    @input : 
        list : lst_tab : liste de 0 ou 1 
            exemple : [0 , 1 , 0 , 1 , 1 , 0]
    
    @output : 
        str :  contient le "VALUES" pour l'envoie de donné à la base de donnée
    '''    
    (cursor, connection) = connect_2_bdd()
    print("data = ", data)
    requete = "INSERT INTO PHOTO (ID_TAB_PHT, REF_PHT, ID_RDE_PHT) VALUES " + data
    print(requete)
    
    cursor.execute(requete)

    connection.commit()
    
    #print(connection)
    disconnect_2_bdd(connection)
    #print(connection)

'''
"""
PHASE DE TEST
"""
data = "(0,0,1),(1,1,1),(2,0,1),(3,1,1),(4,1,1),(5,0,1);"    
add_pht_bdd(data)
'''



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

'''
data = "(000, '2022-05-03 16:29:32.555116');"
add_ronde_bdd(data)
'''