<?php
session_start();
$_SESSION['risp2.1'] = $_POST['Q1'];
$_SESSION['risp2.2'] = $_POST['Q2'];
$_SESSION['risp2.3'] = $_POST['Q3'];
$_SESSION['risp2.4'] = $_POST['Q4'];
$_SESSION['risp2.5'] = $_POST['Q5'];

header('Location:/../foodrecsys3.0/html/form2.html');
?>
