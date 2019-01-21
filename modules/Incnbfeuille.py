import requests
#fonction appele lors du deroulement d'une feuille, va effectuer une requete php vers un serveur qui va incrementer le nombre de feuille distribuer.
#ces donnees sont utile pour le site internet afin de creer des statistiques
def incrementerNombreFeuille():
	userdata={"test":"test2"} #permet d envoyer des donnees sur le serveur
	resp = requests.post('http://thomasfaure05.alwaysdata.net/php/distributeur_requests.php',data = userdata) #incremente via une requete php le nombre de feuille consomme