import RPi.GPIO as GPIO
from Script_Segmentation import lancement_traitement
from main_send_bdd import main
import time


GPIO.setmode(GPIO.BOARD)
channel = 3
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
while True:
    print("Cou")
    if GPIO.input(channel) == 1:
        print("Je suis là")
        lancement_traitement()
        print("Je suis toujours là")
        
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
        