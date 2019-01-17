<?php $host = "publicsql-1.pulseheberg.net";
$user = "service_33670";
$password = "m6YXp34n4j";
$database = "service_33670";

$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);

$stmt = $pdo->prepare('UPDATE Faso_etat SET etat =  1 WHERE ( id = 1 )');
$stmt->execute();

header("Location: http://thomasfaure05.alwaysdata.net");
exit;


