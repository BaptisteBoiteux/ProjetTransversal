from admin_bdd import connect_2_bdd, disconnect_2_bdd

def add_pht_bdd():
    (cursor, connection) = connect_2_bdd()
    
    cursor.execute("SELECT * FROM UTILISATEUR")
    #print(cursor)
    #print(connection)
    
    disconnect_2_bdd(connection)
    
    #print(connection)
    
add_pht_bdd()