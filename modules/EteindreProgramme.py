import requests
import os
#fonction qui permet d'eteindre le programme en envoyant une requete php au serveur, qui va actualiser le status du programme
def Eteindre_prog():
 	#envoie une notification sur le telephone de l utilisateur
        os.system('../pushbullet.sh "Le distributeur d\'essuie-tout est vide !"') #envoi une notification sur pushbullet
	userdata ={"":""}
	resp= requests.post('http://thomasfaure05.alwaysdata.net/php/desactiverProgramme.php',data= userdata) #fait une requete php permettant de stopper automatiquement le programme
	print "Alerte : programme eteint pour cause de manque de stock"
