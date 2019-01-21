# fonction qui verifie grace a une base de donnee en externe si le programem est allume ou pas
import requests
#permet de verifier d'apres le serveur si le programme est annule ou pas en envoyant une requete php qui va retourner
# l'etat du programme, "1"= allume, "0"=eteint
def est_allumer():
	userdata={"":""} #permet d envoyer des informations au serveur
	resp = requests.post('http://thomasfaure05.alwaysdata.net/php/verifierEtat.php',data = userdata) #requete php vers un de nos serveurs
	return resp.text=="1" #compare le resultat , la requete renvoie 1 quand le programme est allume, 0 sinon