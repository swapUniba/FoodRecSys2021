<?php
session_start();
$_SESSION['risp3.1'] = $_POST['Q1'];
$_SESSION['risp3.2'] = $_POST['Q2'];
$_SESSION['risp3.3'] = $_POST['Q3'];
$_SESSION['risp3.4'] = $_POST['Q4'];
$_SESSION['risp3.5'] = $_POST['Q5'];


$header = "altezza, peso, sesso, età, sport, occupazione, esperienza_web, esperienza_cucina, obiettivo, query1, nomericettasinistra1, nomericettadestra1, ordinamentosinistra1, ordinamentodestra1, preferenza1, saporito1, sano1, perd/prend_peso1, facile1, etichette_mostrate1, query2, nomericettasinistra2, nomericettadestra2, ordinamentosinistra2, ordinamentodestra2, preferenza2, saporito2, sano2, perd/prend_peso2, facile2, etichette_mostrate2, query3, nomericettasinistra3, nomericettadestra3, ordinamentosinistra3, ordinamentodestra3, preferenza3, saporito3, sano3, perd/prend_peso3, facile3, etichette_mostrate3 ";

$text = $_SESSION['altezza'].", ".$_SESSION['peso'].", ".$_SESSION['sesso'].", ".$_SESSION['eta'].", ".$_SESSION['sport'].", ".$_SESSION['occupazione'].", ".$_SESSION['esperienza_web'].", ".$_SESSION['esperienza_cucina'].", ".$_SESSION['obiettivo'].', '.$_SESSION['oplifestyle'].', '.$_SESSION['conslifestyle'].', '.$_SESSION['query1'].', '.$_SESSION['nomericettasinistra1'].', '.$_SESSION['nomericettadestra1'].', '.$_SESSION['ordinamentosinistra1'].', '.$_SESSION['ordinamentodestra1'].', '.$_SESSION['risp1.1'].', '.$_SESSION['risp1.2'].', '.$_SESSION['risp1.3'].', '.$_SESSION['risp1.4'].', '.$_SESSION['risp1.5'].', '.$_SESSION['etichette1'].', '.$_SESSION['query2'].', '.$_SESSION['nomericettasinistra2'].', '.$_SESSION['nomericettadestra2'].', '.$_SESSION['ordinamentosinistra2'].', '.$_SESSION['ordinamentodestra2'].', '.$_SESSION['risp2.1'].', '.$_SESSION['risp2.2'].', '.$_SESSION['risp2.3'].', '.$_SESSION['risp2.4'].', '.$_SESSION['risp2.5'].', '.$_SESSION['etichette2'].', '.$_SESSION['query3'].', '.$_SESSION['nomericettasinistra3'].', '.$_SESSION['nomericettadestra3'].', '.$_SESSION['ordinamentosinistra3'].', '.$_SESSION['ordinamentodestra3'].', '.$_SESSION['risp3.1'].', '.$_SESSION['risp3.2'].', '.$_SESSION['risp3.3'].', '.$_SESSION['risp3.4'].', '.$_SESSION['risp3.5'].', '.$_SESSION['etichette3'] ;


if(file_put_contents('dati_raccolti.txt', $text.PHP_EOL , FILE_APPEND | LOCK_EX)){

	$randomNumber = rand(1000000,9999999);
    session_destroy();


}



?>
