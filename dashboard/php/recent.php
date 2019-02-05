<?php $host = "publicsql-1.pulseheberg.net";
    $user = "service_33670";
   $password = "m6YXp34n4j";
    $database = "service_33670";
	
$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);


for($i=0;$i<5;++$i) {
    $stmt = $pdo->prepare('SELECT * FROM Projet_FASO where date=:date');

    if ($stmt->execute(array('date' => date("Y-m-d", strtotime(' -' . $i . ' day'))))) {
        if ($stmt->rowCount() == 0) {
	
            $stmt = $pdo->prepare('INSERT INTO Projet_FASO(quantite, date) VALUES (:quantite,:date)');
            $stmt->execute(array(
                'quantite' => "0",
                'date' => date("Y-m-d", strtotime(' -' . $i . ' day'))));
        }
    }
}

		$tableau=array();
		$stmt = $pdo->prepare('SELECT * FROM Projet_FASO ORDER BY date DESC LIMIT 5');
        if ($stmt->execute()) {
            foreach ($stmt as $row) {
                $tableau[]=$row;
            }
     
        }
		//var_dump($tableau);
		

echo json_encode($tableau);
        

         
