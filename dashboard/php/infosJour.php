<?php $host = "publicsql-1.pulseheberg.net";
    $user = "service_33670";
   $password = "m6YXp34n4j";
    $database = "service_33670";
	
$pdo = new PDO('mysql:host='.$host.';dbname='.$database, $user, $password);
        
		$tableau=array();
		$stmt = $pdo->prepare('SELECT * FROM Projet_FASO WHERE date=:date ORDER BY date ASC LIMIT 5');
        if ($stmt->execute(array('date' => date("Y-m-d")))) {
            foreach ($stmt as $row) {
                $tableau[]=$row;
            }
     
        }
        if(sizeof($tableau)==0){
            $row["date"]= date("Y-m-d");
            $row["quantite"]=0;
            $tableau[]=$row;
        }
		//var_dump($tableau);
		

echo json_encode($tableau);
        

         