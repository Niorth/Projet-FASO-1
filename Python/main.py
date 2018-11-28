import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet
from ChangerCouleur import ChangerCouleur


# main a recuperer sur le pc qui va appeler calculerRestantSopalin()

def DeroulerFeuille(coef):
	fwd()
	time.sleep(5)
	stop()
	time.sleep(4)
	main()

def calculerRestantSopalin():
    ultrasonic_ranger = 7
    valeurCapteur = 1
    try:
        valeurCapteur = ultrasonicRead(ultrasonic_ranger)  # mettre notre fonction capteur
    except TypeError:
        print "Error"
    distanceCapteurRouleau = 30  # valeur constante a calculer
    from ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur)
    if (valeurCapteur < distanceCapteurRouleau):
        print("peut derouler")
        from CalculerCoef import CalculerCoef
        coef = CalculerCoef(valeurCapteur, distanceCapteurRouleau)
        DeroulerFeuille(coef);
    else:
        print("peut pas derouler")




def main():

    try:
        print("test")
        ChangerCouleur(ultrasonicRead(7))
    except:
        print("le systeme ne peut fonctionner")
    capteur_main = 8
    main = False
    valeur = 11
    while (main == False):
       
        try:
            valeur = ultrasonicRead(capteur_main)
        except:
            print("error")
        if (valeur < 10):
            print("main trouve")
            main = True
            calculerRestantSopalin()
	

main()
