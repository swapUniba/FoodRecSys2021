<?php
session_start();
$_SESSION['risp1.1'] = $_POST['Q1'];
$_SESSION['risp1.2'] = $_POST['Q2'];
$_SESSION['risp1.3'] = $_POST['Q3'];
$_SESSION['risp1.4'] = $_POST['Q4'];
$_SESSION['risp1.5'] = $_POST['Q5'];
$_SESSION['risp1.6'] = $_POST['Q6'];


header('Location:/../foodrecsys3.0/html/form3.html');
?>



   