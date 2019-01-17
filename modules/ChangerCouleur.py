import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
def ChangerCouleur(distance,cpt):
    ledVerte = 4
    ledRouge = 2
    ledOrange = 3
    distanceSopalinInit = 9  # valeur rouleau plein
    distanceSopalinVide = 12 # valeur du rouleau quand il est vide
    pourcentageRestant = 100 - ((distanceSopalinInit - distance) * -(100/(distanceSopalinVide-distanceSopalinInit))) #calcul du pourcentage restant
    if (pourcentageRestant > 50):
        digitalWrite(ledVerte, 1)
        digitalWrite(ledOrange, 0)
        digitalWrite(ledRouge, 0)

    elif (pourcentageRestant > 10):
        digitalWrite(ledVerte, 0)
        digitalWrite(ledOrange, 1)
        digitalWrite(ledRouge, 0)
    else:
	if(cpt > 10):
        	digitalWrite(ledVerte, 0)
        	digitalWrite(ledOrange, 0)
        	digitalWrite(ledRouge, 1)
	else:
		digitalWrite(ledVerte, 0)
		digitalWrite(ledOrange, 1)
		digitalWrite(ledRouge, 0)
