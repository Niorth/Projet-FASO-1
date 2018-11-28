import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet
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
        from main import DeroulerFeuille
        DeroulerFeuille(coef);
    else:
        print("peut pas derouler")



