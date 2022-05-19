import RPi.GPIO as GPIO
from Script_Segmentation import lancement_traitement
from main_send_bdd import main
import time


GPIO.setmode(GPIO.BOARD)
channel = 21
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
while True:
    time.sleep(2)
    #print("Cou")
    if GPIO.input(channel):
        print("Coucou")
        lancement_traitement()
        
        flag = False
        with open("Larry_Ronde_Info.txt", "r") as file :
            l = file.readlines()
            print(int(l[0]))
            if int(l[0]) == 5:
                flag = True
            
            
        if flag:
            main()



def dernier_tab():
    flag = False
    with open("Larry_Ronde_Info.txt", "r") as file :
        l = file.readlines()
        if int(l[0]) == 0:
            flag = True
            
    return flag
        