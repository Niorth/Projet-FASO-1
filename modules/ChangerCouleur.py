import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
#fonction qui va permettre de changer la couleur des leds en fonction d'une distance donnee en parametre,
# le compteur lui sert simplement a afficher rouge lorsque l'on depasse les 10 deroulements quand le rouleau est vide
def ChangerCouleur(distance,cpt):
    ledVerte = 4
    ledRouge = 2
    ledOrange = 3
    distanceSopalinInit = 9  # valeur rouleau plein
    distanceSopalinVide = 12 # valeur du rouleau quand il est vide
    pourcentageRestant = 100 - ((distanceSopalinInit - distance) * -(100/(distanceSopalinVide-distanceSopalinInit))) #calcul du pourcentage restant
    print pourcentageRestant
    if (pourcentageRestant > 50): #stock a plus de 50 pourcents , lumiere verte
        digitalWrite(ledVerte, 1)
        digitalWrite(ledOrange, 0)
        digitalWrite(ledRouge, 0)

    elif (pourcentageRestant > 10): #stock superieur a 10 pourcents, lumiere orange/bleu
        digitalWrite(ledVerte, 0)
        digitalWrite(ledOrange, 1)
        digitalWrite(ledRouge, 0)
    else:
	if(cpt >= 10 or  distance >20): #si compteur >=10 on passe a la couleur rouge
        	digitalWrite(ledVerte, 0)
        	digitalWrite(ledOrange, 0)
        	digitalWrite(ledRouge, 1)
	else:                           # si compteur <10 on passe a la couleur orange/bleu
		digitalWrite(ledVerte, 0)
		digitalWrite(ledOrange, 1)
		digitalWrite(ledRouge, 0)
