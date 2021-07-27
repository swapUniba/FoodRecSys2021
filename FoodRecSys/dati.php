<?php
session_start();

$_SESSION['altezza'] = $_POST['altezza'];
$_SESSION['peso']= $_POST['peso'];
$_SESSION['sesso']= $_POST['sesso'];
$_SESSION['eta'] = $_POST['age'];
$_SESSION['sport']= $_POST['sport'];
$_SESSION['occupazione']= $_POST['occupation'];
$_SESSION['esperienza_web'] = $_POST['websiteUsage'];
$_SESSION['esperienza_cucina']= $_POST['exp'];
$_SESSION['obiettivo'] = $_POST['goal'];
$_SESSION['oplifestyle']=$_POST['HS'];
$_SESSION['conslifestyle']=$_POST['HC'];


header('Location: html/form.html');
?>