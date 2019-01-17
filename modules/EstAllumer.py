# fonction qui verifie grace a une base de donnee en externe si le programem est allume ou pas
import requests
def est_allumer():
	userdata={"test":"test2"}
	resp = requests.post('http://thomasfaure05.alwaysdata.net/php/verifierEtat.php',data = userdata)
	return resp.text=="1"