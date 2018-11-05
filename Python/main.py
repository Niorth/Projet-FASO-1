
from gopigo import *
import time,math
from grovepi import *
#main a recuperer sur le pc qui va appeler calculerRestantSopalin()

def initialisation():
	

def calculerRestantSopalin():
	valeurCapteur = #mettre notre fonction capteur
	distanceCapteurRouleau = #valeur constante à calculer
	ChangerCouleur(valeurCapteur)
	if(valeurCapteur < distanceCapteurRouleau):
		print("peut derouler")
		coef = CalculerCoef(valeurCapteur,distanceCapteurRouleau)
		DeroulerFeuille(coef);
		ChangerCouleur(valeurCapteur)
	else:
		print("peut pas derouler")



def ChangerCouleur(distance):
	ledVerte= 2
	ledRouge= 3
	ledOrange= 4
	distanceSopalinInit=#valeur rouleau plein
	pourcentageRestant=(distance/distanceSopalinInit)*100
	if(pourcentageRestant > 50):
		digitalWrite(ledVerte,1)
		digitalWrite(ledOrange,0)
		digitalWrite(ledRouge,0)
	
	elif(pourcentageRestant > 10):
		digitalWrite(ledVerte,0)
		digitalWrite(ledOrange,1)
		digitalWrite(ledRouge,0)
	else:
		digitalWrite(ledVerte,0)
		digitalWrite(ledOrange,0)
		digitalWrite(ledRouge,1)



def CalculerCoef(valeurCapteur,distanceCapteurRouleau):
	L = #longeur d'une feuille
	D = #largeur d'un rouleur vide + (distanceCapteurRouleau - valeurCapteur)*2
	perimetre = math.pi*D
	return (L/perimetre)*360

def DeroulerFeuille(coef):
	disable_servo()
	for i in range(coef):
		servo(i)
		print i
		time.sleep(.01)



		


