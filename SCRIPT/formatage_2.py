def formatage_2(lst_tab, id_rde):
    '''
    @input : 
        list : lst_tab : liste de 0 ou 1 
            exemple : [0 , 1 , 0 , 1 , 1 , 0]
        int :  id_rde  : id de la ronde correspondant
    
    @output : 
        str :  contient le "VALUES" pour l'envoie de donné à la base de donnée
    '''    
    output = ""
    
    for index in range(len(lst_tab)):
        output += "("+ str(index) +","+ str(lst_tab[index]) +","+ str(id_rde) +")"
        if (index < len(lst_tab) -1 ):
            output += ","
        else: 
            output += ";"

    #print(output)
