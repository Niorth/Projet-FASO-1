<?php $host = "publicsql-1.pulseheberg.net";
$user = "service_33670";
$password = "m6YXp34n4j";
$database = "service_33670";

$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);


$tableau=array();

$stmt = $pdo->prepare('SELECT * FROM Projet_FASO WHERE YEAR(date) = :year');
if ($stmt->execute(array('year' => date("Y")))) {
    foreach ($stmt as $row) {
        $row["mois"]=date("m",strtotime($row["date"]));
        $tableau[]=$row;
    }

}
//var_dump($tableau);


echo json_encode($tableau);


