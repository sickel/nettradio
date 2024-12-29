<?php

class returndata{}

$ret = new returndata;

if(array_key_exists('kanal',$_GET)){
if($_GET['kanal']=='kanal'){
	returnkanal();
}
}
$line = '';
$rettext = '';
$file='/var/www/radiotitle';

$f = fopen($file , 'r');
$cursor = -1;

fseek($f, $cursor, SEEK_END);
$char = fgetc($f);

/**
 * Trim trailing newline chars of the file
 */
while ($char === "\n" || $char === "\r") {
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}

/**
 * Read until the start of file or first newline char
 */
while ($char !== false && $char !== "\n" && $char !== "\r") {
    /**
     * Prepend the new char
     */
    $line = $char . $line;
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}
if(str_contains($line,'=')){
    $exp=explode('=',$line,2);
    $line=ltrim($exp[1],"'");
    $rettext=rtrim($line,"';");
}elseif(str_contains($line,':')){
    $exp=explode(':',$line,2);
    $rettext=$exp[1];
}
$ret->text=$rettext;

$file = fopen('/var/www/html/ch.txt',"r");
$ret->ch = fgets($file);

$amix=`/usr/bin/amixer -M`;
preg_match('/\[([0-9]+)%\]/',$amix,$vol);
$ret->vol=$vol[1];

echo json_encode($ret);



?>
