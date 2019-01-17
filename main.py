import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
import requests
import urllib2
from grovepi import *
import os  # pour PushBullet

#compteur avant d'afficher plus de stock
global cpt
cpt = 0
def DeroulerFeuille(coef):
	from modules.Incnbfeuille import incrementerNombreFeuille
	incrementerNombreFeuille()
	tmpRotation = (coef*1.5)/360
	print "Duree rotation : ",tmpRotation
	if(tmpRotation>=0):
	    fwd()
	    time.sleep(tmpRotation)
	    stop()
	time.sleep(4)
 	main()

def calculerRestantSopalin():
    print "/////////////////////////////"
    print "          Dispenser          "
    print "/////////////////////////////"
    ultrasonic_ranger = 7
    valeurCapteur = 1
    global cpt
    try:
        valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))  # mettre notre fonction capteur
    except TypeError:
        print "Error"
    distanceCapteurRouleau = 12  # valeur constante
    from modules.ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur,cpt)
    print "Distance Capteur Rouleau: ",valeurCapteur
    if(valeurCapteur > 13):
        from modules.EteindreProgramme import Eteindre_prog
	Eteindre_prog()
	main()
    elif (valeurCapteur < distanceCapteurRouleau or cpt < 10):
	if(valeurCapteur >= distanceCapteurRouleau):
		cpt = cpt+1
	if(valeurCapteur < distanceCapteurRouleau):
		cpt = 0
        print("Etat : peut derouler")
        from modules.CalculerCoef import CalculerCoef
        coef = CalculerCoef(valeurCapteur, distanceCapteurRouleau)
	print "Degres de rotation : ",coef
	print "Compteur de non stock : ",cpt
	DeroulerFeuille(coef);
	
    else:
        print("Etat : ne peut pas derouler")
	from modules.EteindreProgramme import Eteindre_prog
	Eteindre_prog()
	main()
	

def main():

    capteur_main = 8
    main = False
    valeur = 11
    while (main == False):
       
        try:
            valeur = ultrasonicRead(capteur_main)
        except:
            print("Alerte : erreur de capteur")
	from modules.EstAllumer import est_allumer
        if (valeur < 5 and est_allumer()):
            print("Alerte : main trouve")
            main = True
            calculerRestantSopalin()
	
def init():
    ultrasonic_ranger = 7
    try:
        valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))
    except TypeError:
	print("error")
    #jeu de couleur pour montrer que le systeme s'allume
    ledVerte = 4
    ledOrange = 3
    ledRouge = 2
    cptEssai = 0
    doitReboot= True
    #on fait 10 tentatives avant le reboot
    while(cptEssai<10 and doitReboot== True):
    	print(doitReboot)
	#jeu de couleur montrant une tentative
	for i in range(0,10):
    		digitalWrite(ledVerte, 1)
    		digitalWrite(ledOrange, 0)
    		digitalWrite(ledRouge, 0)
    		time.sleep(0.1)
    		digitalWrite(ledVerte, 0)
    		digitalWrite(ledOrange, 1)
    		digitalWrite(ledRouge, 0)
    		time.sleep(0.1)
    		digitalWrite(ledVerte, 0)
    		digitalWrite(ledOrange, 0)
    		digitalWrite(ledRouge, 1)
    		time.sleep(0.1)
    		digitalWrite(ledVerte, 0)
    		digitalWrite(ledOrange, 0)
    		digitalWrite(ledRouge, 0)
		time.sleep(0.1)
	try:
	    urllib2.urlopen(urllib2.Request('http://google.fr'))
	    doitReboot = False
	    print(doitReboot)
	except:
	    #si la connection internet n'est pas active la couleur rouge apparait
	    for i in range(0,3):
	    	digitalWrite(ledVerte, 0)
            	digitalWrite(ledOrange, 0)
            	digitalWrite(ledRouge, 1)
		time.sleep(0.1)
		digitalWrite(ledVerte, 0)
                digitalWrite(ledOrange, 0)
                digitalWrite(ledRouge, 0)
		time.sleep(0.1)
	    cptEssai = cptEssai + 1		    
    if(doitReboot):
	os.system('sudo reboot')
    else:
	#la couleur vert apparait car internet est active, on passe par la suite dans le programme principale
	for i in range(0,3):
               	digitalWrite(ledVerte, 1)
               	digitalWrite(ledOrange, 0)
                digitalWrite(ledRouge, 0)
                time.sleep(0.1)
                digitalWrite(ledVerte, 0)
                digitalWrite(ledOrange, 0)
                digitalWrite(ledRouge, 0)
                time.sleep(0.1)
    from modules.ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur,cpt)
    main()

init()
