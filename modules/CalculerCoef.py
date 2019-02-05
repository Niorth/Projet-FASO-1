import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet
#fonction qui va calculer le coefficient de rotation que devra effectuer le moteur, avec la distance donne par le capteur et la distance (constante donne) lorsque le rouleau est vide
#va retourner un degre de rotation
def CalculerCoef(valeurCapteur,distanceCapteurRouleau):
	L = 23 #longeur d'une feuille
	D = (2 + (distanceCapteurRouleau - valeurCapteur)) * 2 #largeur d'un rouleur vide + (distanceCapteurRouleau - valeurCapteur)*2
	print(D)
	perimetre = math.pi*D
	print(perimetre)
	return (L*360)/perimetre
