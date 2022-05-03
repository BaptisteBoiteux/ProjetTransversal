from datetime import datetime


def formatage_1():
    output = ""
    DATE_RDE = datetime.now()
    #print (DATE_RDE)
    TPS_RDE = str('000')
    output = '(' +  TPS_RDE + ", " + "'" + str(DATE_RDE) + "'" + ')' + ';'
    return output
print (formatage_1())
