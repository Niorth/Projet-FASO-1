import requests
import os
def Eteindre_prog():
 	#envoie une notification sur le telephone de l utilisateur
        os.system('../pushbullet.sh "Il faudra penser a acheter du Sopalin ;) "')
	userdata ={"test":"test2"}
	resp= requests.post('http://thomasfaure05.alwaysdata.net/php/desactiverProgramme.php',data= userdata)
	print "Alerte : programme eteint pour cause de manque de stock"
