from add_2_bdd import *
from admin_bdd import *
from formatage import *

def main (lst_tab):
    
    # Ajout dans la table RONDE
    add_ronde_bdd( formatage_1() )
    print("Succès : Ajout dans la table RONDE")
    

    # Ajout dans la table PHOTO
    data = formatage_2( lst_tab, get_id_ronde() )
    add_pht_bdd( data )
    print("Succès : Ajout dans la table PHOTO")
    
    
main([0,0,1,0,0,1,1,0])