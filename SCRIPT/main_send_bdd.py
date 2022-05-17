from add_2_bdd import *
from admin_bdd import *
from formatage import *

max_tableau = 4

def main ():
    lst_tab = get_data_txt()
    # Ajout dans la table RONDE
    add_ronde_bdd( formatage_1() )
    print("Succès : Ajout dans la table RONDE")
    

    # Ajout dans la table PHOTO
    data = formatage_2( lst_tab, get_id_ronde() )
    add_pht_bdd( data )
    print("Succès : Ajout dans la table PHOTO")
    
def get_data_txt():
    lst_tab = []
    with open("Larry_Ronde_Info.txt", "r") as file :
        l = file.readlines()
        it = int(l[0])
        for i in range(1,len(l)):
            lst_tab.append(int(l[i]))
    
    return lst_tab

