<?php

$amix="/usr/bin/amixer";
$step='5%';
$adj='nonset';

if (isset($_GET)){
    $adj='down';
    if ($_GET['adjust']=='up'){
        $adj='up';
    }
}

if ($adj=='up'){
    $adjust="${step}+";}
else {
    $adjust="${step}-";}

$ch="'PCM'";

$amx="$amix set $ch $adjust -M"; 

$output=`$amx`;
preg_match('/\[([0-9]+)%\]/',$output,$vol);
$ret->vol=$vol[1];
echo json_encode($ret);

?>
