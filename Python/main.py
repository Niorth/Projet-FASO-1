import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet
from ChangerCouleur import ChangerCouleur


# main a recuperer sur le pc qui va appeler calculerRestantSopalin()

def DeroulerFeuille(coef):
	#print(coef)
	fwd()
	time.sleep(5)
	stop()
	time.sleep(4)
	main()

def main():

    try:
        ChangerCouleur(ultrasonicRead(7))
    except:
        print("le systeme ne peut fonctionner")
    capteur_main = 8
    main = False
    valeur = -1
    while (main == False):
        try:
            valeur = ultrasonicRead(capteur_main)
        except:
            print("error")
        if (valeur < 10):
            print("main trouve")
            main = True
	from CalculerRestantSopalin import calculerRestantSopalin
    calculerRestantSopalin()


main()
