import RPi.GPIO as GPIO
from Script_Segmentation import Detection

GPIO.setmode(GPIO.BOARD)

channel = 21
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')
    
def lancement_traitement():
    if GPIO.input(channel):
        traitement = Detection('Larry_Ronde_Info.txt')
    else:
        print('Marche pas')
        
lancement_traitement()