
from gopigo import *
import time,math
from grovepi import *
import os #pour PushBullet
#main a recuperer sur le pc qui va appeler calculerRestantSopalin()

	
def calculerRestantSopalin():
	ultrasonic_ranger = 7
	valeurCapteur = 1
	try:
		valeurCapteur = ultrasonicRead(ultrasonic_ranger) #mettre notre fonction capteur
	except TypeError:
		print "Error"	
	distanceCapteurRouleau = 30 #valeur constante a calculer
	ChangerCouleur(valeurCapteur)
	if(valeurCapteur < distanceCapteurRouleau):
		print("peut derouler")
		coef = CalculerCoef(valeurCapteur,distanceCapteurRouleau)
		DeroulerFeuille(coef);
	else:
		print("peut pas derouler")
		
	

def ChangerCouleur(distance):
	ledVerte= 4
	ledRouge= 2
	ledOrange= 3
	distanceSopalinInit= 10#valeur rouleau plein
	distanceSopalinVide= 20
	#print(distance)
	pourcentageRestant=(distanceSopalinVide - distance) * 10 
	print pourcentageRestant
	if(pourcentageRestant > 50):
		digitalWrite(ledVerte,1)
		digitalWrite(ledOrange,0)
		digitalWrite(ledRouge,0)
	
	elif(pourcentageRestant > 10):
		digitalWrite(ledVerte,0)
		digitalWrite(ledOrange,1)
		digitalWrite(ledRouge,0)
	else:
	        os.system('../pushbullet.sh "Frero il faudra penser a acheter du Sopalin ;) "')
		digitalWrite(ledVerte,0)
		digitalWrite(ledOrange,0)
 		digitalWrite(ledRouge,1)


def CalculerCoef(valeurCapteur,distanceCapteurRouleau):
	L = 30 #longeur d'une feuille
	D = 5 #largeur d'un rouleur vide + (distanceCapteurRouleau - valeurCapteur)*2
	perimetre = math.pi*D
	return (L/perimetre)*360

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
		print("Le RoUlEaU EsT CaSsE")
	capteur_main=8
	main = False
	valeur = 0
	while(main==False):
		try :
			valeur = ultrasonicRead(capteur_main)
		except:	
			print("error")
		if(valeur<10):
			main=True
	calculerRestantSopalin()
		


main()
