import sys
#on appelle la bibliotheque
sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
import requests
import urllib2
from grovepi import *
#compteur avant d'afficher plus de stock
global cpt
cpt = 0
#determine si on est hors-ligne ou non
global modeHorsLigne
modeHorsLigne = False

#Fonction qui permet de derouler une feuille en fonction du coef
#va calculer le temps de rotation necessaire par rapport au coef et va faire tourner le moteur
def DeroulerFeuille(coef):
	global modeHorsLigne
	#si on a la connexion internet active, on incremente le nombre de feuille consomme
	if(modeHorsLigne == False):
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

#fonction qui permet de calculer le restant de papier, et effectue differente tache en fonction du pourcentage restant(envoi de notifications...)
def calculerRestantSopalin():
    print "/////////////////////////////"
    print "          Dispenser          "
    print "/////////////////////////////"
    ultrasonic_ranger = 7
    valeurCapteur = 1
    global cpt
    global modeHorsLigne
	#on essaye de lire la valeur donne par le capteur
    try:
        valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))  # mettre notre fonction capteur
    except TypeError:
        print "Error"
    distanceCapteurRouleau = 13  # valeur constante entre rouleau vide et le capteur
    from modules.ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur,cpt)
    print "Distance Capteur Rouleau: ",valeurCapteur
    if(valeurCapteur < distanceCapteurRouleau-1):
    	cpt = 0
	#si on a plus de stock, correspond au fait que aucun rouleau n est present sur le dispositif, inutile donc de derouler
    if(valeurCapteur > 13):
	if(modeHorsLigne == False):
        	from modules.EteindreProgramme import Eteindre_prog
		Eteindre_prog()
	cpt=10 #on place le compteur a 10 afin d interdire le deroulement d une feuille
	ChangerCouleur(valeurCapteur, cpt)
	main()
    elif (valeurCapteur <= distanceCapteurRouleau and cpt < 10): 
	if(valeurCapteur >= distanceCapteurRouleau-1): #-1 pour etre sur qu'il compte, ce n'est pas du hasard, comme nous jouons sur 3cm il se peut que le capteur fasse un arrondi
		cpt = cpt+1
        print("Etat : peut derouler")
        from modules.CalculerCoef import CalculerCoef
        coef = CalculerCoef(valeurCapteur, distanceCapteurRouleau)
	print "Degres de rotation : ",coef
	print "Compteur de non stock : ",cpt
	DeroulerFeuille(coef);
    else:
        print("Etat : ne peut pas derouler")
	if(modeHorsLigne==False): #si la connexion est active,on eteind le programme
		from modules.EteindreProgramme import Eteindre_prog
		Eteindre_prog()
	main() #on decide de ne pas derouler, on retourne donc dans le main en attendant une nouvelle demande de l utilisateur

#permet de verifier la connexion internet
def VerifierCon(valeur):
	ledVerte = 4  # id led verte
	ledOrange = 3  # id led Bleu/Orange
	ledRouge = 2  # id led Rouge
	ultrasonic_ranger = 7 #capteur de stock
	global modeHorsLigne
	global cpt
	valeurCapteur= 1
	try:
		valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))  # mettre notre fonction capteur
	except TypeError:
		print
		"Error"
	# on test ici si la connexion internet fonctionne pour basculer de mode
	if(valeur < 5 and modeHorsLigne == True):
		try:
			urllib2.urlopen(urllib2.Request('http://google.fr'))  # on effectue une tentative de connexion a une url pour verfier la connexion
			#on passe en mode en-ligne

			modeHorsLigne = False
			print "on passe en-ligne"
			for i in range(0, 3):
				digitalWrite(ledVerte, 1)
				digitalWrite(ledOrange, 0)
				digitalWrite(ledRouge, 0)
				time.sleep(0.1)
				digitalWrite(ledVerte, 0)
				digitalWrite(ledOrange, 0)
				digitalWrite(ledRouge, 0)
				time.sleep(0.1)
			if(valeurCapteur>13):
				cpt=10 #on met 10 afin d'avoir la couleur rougeps
			from modules.ChangerCouleur import ChangerCouleur
			ChangerCouleur(valeurCapteur, cpt)
		except:

			print "on reste en hors-ligne"
	if (valeur < 5 and modeHorsLigne == False):
		print "on est en ligne de base"
		try:
			urllib2.urlopen(urllib2.Request(
				'http://google.fr'))  # on effectue une tentative de connexion a une url pour verfier la connexion
			print "on reste en en-ligne"

		except:
			# on passe en mode hors-ligne
			modeHorsLigne = True
			print "on passe horsligne"
			for i in range(0, 3):
				digitalWrite(ledVerte, 0)
				digitalWrite(ledOrange, 0)
				digitalWrite(ledRouge, 1)
				time.sleep(0.1)
				digitalWrite(ledVerte, 0)
				digitalWrite(ledOrange, 0)
				digitalWrite(ledRouge, 0)
				time.sleep(0.1)
			from modules.ChangerCouleur import ChangerCouleur
			ChangerCouleur(valeurCapteur, cpt)
		#fonction principale du projet, c'est ici que l'on va gerer la detection de main et du coup de lancer la fonction DeroulerFeuille() quand une main est presente
def main():
    global modeHorsLigne
    global cpt
    capteur_main = 8
    main = False
    valeur = 11
    while (main == False):
        time.sleep(0.2)
        try:
            valeur = ultrasonicRead(capteur_main)
        except:
            print("Alerte : erreur de capteur")
	VerifierCon(valeur)
	from modules.EstAllumer import est_allumer
	if(valeur < 5 and modeHorsLigne == True):
	    print("mode horsligne : main trouve")
            main = True
	    calculerRestantSopalin()
	elif( modeHorsLigne == False):
            if (valeur < 5 and est_allumer()):
            	print("Alerte : main trouve")
            	main = True
            	calculerRestantSopalin()

#fonction d'initialisation qui se lance au demarrage du programme, va determiner si l'on est en mode hors-ligne ou pas
#on va faire plusieurs tentative de connexion afin de permettre a l'utilisateur d'avoir le temps de brancher le cable ethernet si il l'a oublie
def init():
    global modeHorsLigne
    global cpt
    ultrasonic_ranger = 7
    #jeu de couleur pour montrer que le systeme s'allume
    ledVerte = 4 #id led verte
    ledOrange = 3 #id led Bleu/Orange
    ledRouge = 2 #id led Rouge
    cptEssai = 0 #nombre d'essaie de connexion
    sansInternet= True #on dit que de base nous n'avons pas internet
    #on fait 10 tentatives avant le reboot
    while(cptEssai<3 and sansInternet== True):
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
	    urllib2.urlopen(urllib2.Request('http://google.fr')) #on effectue une tentative de connexion a une url pour verfier la connexion
	    sansInternet = False
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
    valeurCapteur= 1		    
    if(sansInternet):
	modeHorsLigne = True
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
	valeurCapteur = 1
    try:
	valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))
    except TypeError:
	print "Error"
    if(valeurCapteur >13):
	if (modeHorsLigne == False):
	    from modules.EteindreProgramme import Eteindre_prog
	    Eteindre_prog()
	cpt=10 #on met le compteur a 10 si la valeur est superieur a 13 (le rouleau n est pas present)
    from modules.ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur,cpt) #on met 10 pour mettre automatiquement du rouge
    main()
init()
