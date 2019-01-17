import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet

def ChangerCouleur(distance):
    ledVerte = 4
    ledRouge = 2
    ledOrange = 3
    distanceSopalinInit = 10  # valeur rouleau plein
    distanceSopalinVide = 20
    # print(distance)
    pourcentageRestant = (distanceSopalinVide - distance) * 10
    print pourcentageRestant
    if (pourcentageRestant > 50):
        digitalWrite(ledVerte, 1)
        digitalWrite(ledOrange, 0)
        digitalWrite(ledRouge, 0)

    elif (pourcentageRestant > 10):
        digitalWrite(ledVerte, 0)
        digitalWrite(ledOrange, 1)
        digitalWrite(ledRouge, 0)
    else:
        os.system('../pushbullet.sh "Il faudra penser a acheter du Sopalin ;) "')
        digitalWrite(ledVerte, 0)
        digitalWrite(ledOrange, 0)
        digitalWrite(ledRouge, 1)
