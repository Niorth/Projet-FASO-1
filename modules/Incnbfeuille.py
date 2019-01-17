import requests
def incrementerNombreFeuille():
	userdata={"test":"test2"}
	resp = requests.post('http://thomasfaure05.alwaysdata.net/php/distributeur_requests.php',data = userdata)