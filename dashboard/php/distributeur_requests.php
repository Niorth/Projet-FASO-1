<?php $host = "publicsql-1.pulseheberg.net";
    $user = "service_33670";
   $password = "m6YXp34n4j";
    $database = "service_33670";
	
$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);
        
		
		$stmt = $pdo->prepare('SELECT * FROM Projet_FASO where date=:date');
        if ($stmt->execute(array('date' => date("Y-m-d")))) {
            if($stmt->rowCount()==0){
				$stmt = $pdo->prepare('INSERT INTO Projet_FASO(quantite, date) VALUES (:quantite,:date)');
				$stmt->execute(array(
            'quantite' => "1",
            'date' => date("Y-m-d")));
				echo('insertion faite');
			}else{
				echo('elle existe deja');
				$stmt = $pdo->prepare('UPDATE Projet_FASO SET quantite = quantite + 1 WHERE ( date = :date )');
				$stmt->execute(array(
            'date' => date("Y-m-d")));
			}
        }
        return $tableau;

         