<?php
$step='5%';
$adj='up';

if ($adj=='up'){
    $adjust="${step}+";}
else {
    $adjust="${step}-";}
# print($adjust);
$ch="'Master'";

$amx="/usr/bin/amixer set $ch $adjust -M"; 

$output=`$amx`;
preg_match('/\[([0-9]+)%\]/',$output,$vol);
print_r($vol);
# print($output);
?>
