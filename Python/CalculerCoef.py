import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
from grovepi import *
import os  # pour PushBullet

def CalculerCoef(valeurCapteur,distanceCapteurRouleau):
	L = 30 #longeur d'une feuille
	D = 5 #largeur d'un rouleur vide + (distanceCapteurRouleau - valeurCapteur)*2
	perimetre = math.pi*D
	return (L/perimetre)*360
