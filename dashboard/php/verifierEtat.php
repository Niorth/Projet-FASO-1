<?php $host = "publicsql-1.pulseheberg.net";
$user = "service_33670";
$password = "m6YXp34n4j";
$database = "service_33670";

$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);

$valeur;
$stmt = $pdo->prepare('SELECT etat FROM Faso_etat where id=1');
if ($stmt->execute()) {
    foreach ($stmt as $row) {
        $valeur=$row;
    }

}


echo $valeur["etat"];



